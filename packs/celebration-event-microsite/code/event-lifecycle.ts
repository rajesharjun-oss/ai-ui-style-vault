import type {
  EventLifecycleState,
  IANATimeZone,
  ISODateTime,
  LifecycleConfiguration,
} from "./event-types";

/** Pure reference logic. Server-rendered and transactional products should use the server clock. */

export class EventLifecycleError extends Error {
  constructor(message: string) {
    super(message);
    this.name = "EventLifecycleError";
  }
}

function instant(value: ISODateTime | undefined, label: string): number | undefined {
  if (!value) return undefined;
  const parsed = Date.parse(value);
  if (!Number.isFinite(parsed)) {
    throw new EventLifecycleError(`${label} must be a valid ISO date-time with an explicit offset.`);
  }
  return parsed;
}

function assertTimeZone(timeZone: IANATimeZone): void {
  try {
    new Intl.DateTimeFormat("en", { timeZone }).format(new Date());
  } catch {
    throw new EventLifecycleError(`Unsupported IANA timezone: ${timeZone}`);
  }
}

function localDateKey(value: number, timeZone: IANATimeZone): string {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone,
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(new Date(value));

  const map = Object.fromEntries(parts.map((part) => [part.type, part.value]));
  return `${map.year}-${map.month}-${map.day}`;
}

export function validateLifecycle(config: LifecycleConfiguration): void {
  assertTimeZone(config.timezone);

  const start = instant(config.primaryEventStart, "primaryEventStart")!;
  const end = instant(config.primaryEventEnd, "primaryEventEnd")!;
  if (end <= start) {
    throw new EventLifecycleError("primaryEventEnd must occur after primaryEventStart.");
  }

  const opens = instant(config.rsvpOpensAt, "rsvpOpensAt");
  const closes = instant(config.rsvpClosesAt, "rsvpClosesAt");
  if (opens !== undefined && closes !== undefined && closes <= opens) {
    throw new EventLifecycleError("rsvpClosesAt must occur after rsvpOpensAt.");
  }

  const invitation = instant(config.invitationAnnouncedAt, "invitationAnnouncedAt");
  const saveTheDate = instant(config.saveTheDateAt, "saveTheDateAt");
  if (saveTheDate !== undefined && invitation !== undefined && invitation < saveTheDate) {
    throw new EventLifecycleError("invitationAnnouncedAt cannot precede saveTheDateAt.");
  }

  const post = instant(config.postEventPublishAt, "postEventPublishAt");
  if (post !== undefined && post < end) {
    throw new EventLifecycleError("postEventPublishAt cannot precede the final event end.");
  }

  const archive = instant(config.archiveAt, "archiveAt");
  if (archive !== undefined && archive < end) {
    throw new EventLifecycleError("archiveAt cannot precede the final event end.");
  }
}

export interface LifecycleResult {
  state: EventLifecycleState;
  now: ISODateTime;
  eventTimeZone: IANATimeZone;
  millisecondsUntilNextTransition?: number;
  nextState?: EventLifecycleState;
}

export function resolveEventLifecycle(
  config: LifecycleConfiguration,
  nowInput: Date | ISODateTime = new Date(),
): LifecycleResult {
  validateLifecycle(config);

  const now = nowInput instanceof Date ? nowInput.getTime() : instant(nowInput, "now")!;
  if (!Number.isFinite(now)) throw new EventLifecycleError("now must be valid.");

  const saveTheDate = instant(config.saveTheDateAt, "saveTheDateAt");
  const invitation = instant(config.invitationAnnouncedAt, "invitationAnnouncedAt");
  const rsvpOpen = instant(config.rsvpOpensAt, "rsvpOpensAt");
  const rsvpClose = instant(config.rsvpClosesAt, "rsvpClosesAt");
  const start = instant(config.primaryEventStart, "primaryEventStart")!;
  const end = instant(config.primaryEventEnd, "primaryEventEnd")!;
  const post = instant(config.postEventPublishAt, "postEventPublishAt");
  const archive = instant(config.archiveAt, "archiveAt");

  const result = (state: EventLifecycleState, nextAt?: number, nextState?: EventLifecycleState): LifecycleResult => ({
    state,
    now: new Date(now).toISOString(),
    eventTimeZone: config.timezone,
    ...(nextAt !== undefined && nextAt > now
      ? { millisecondsUntilNextTransition: nextAt - now, nextState }
      : {}),
  });

  if (archive !== undefined && now >= archive) {
    return result("site-archived");
  }

  if (post !== undefined && now >= post) {
    return result("post-event-gallery", archive, archive ? "site-archived" : undefined);
  }

  if (now >= end) {
    return result(
      "event-completed",
      post ?? archive,
      post ? "post-event-gallery" : archive ? "site-archived" : undefined,
    );
  }

  if (now >= start) {
    return result("event-in-progress", end, "event-completed");
  }

  const todayInEventZone = localDateKey(now, config.timezone) === localDateKey(start, config.timezone);
  if (todayInEventZone) {
    return result("event-today", start, "event-in-progress");
  }

  if (rsvpClose !== undefined && now >= rsvpClose) {
    return result("rsvp-deadline-passed", start, "event-today");
  }

  if (rsvpOpen !== undefined && now >= rsvpOpen) {
    return result("rsvp-open", rsvpClose ?? start, rsvpClose ? "rsvp-deadline-passed" : "event-today");
  }

  if (invitation !== undefined && now >= invitation) {
    return result(
      "rsvp-not-open",
      rsvpOpen ?? start,
      rsvpOpen ? "rsvp-open" : "event-today",
    );
  }

  if (saveTheDate !== undefined && now >= saveTheDate) {
    return result(
      "save-the-date",
      invitation ?? rsvpOpen ?? start,
      invitation ? "invitation-announced" : rsvpOpen ? "rsvp-open" : "event-today",
    );
  }

  if (invitation === undefined && saveTheDate === undefined) {
    return result("invitation-announced", rsvpOpen ?? start, rsvpOpen ? "rsvp-open" : "event-today");
  }

  return result("save-the-date", saveTheDate ?? invitation ?? rsvpOpen ?? start, "save-the-date");
}

export function lifecycleCopy(state: EventLifecycleState): string {
  switch (state) {
    case "save-the-date":
      return "Save the date. More celebration details will be shared soon.";
    case "invitation-announced":
      return "The invitation is ready.";
    case "rsvp-not-open":
      return "RSVP will open soon.";
    case "rsvp-open":
      return "Please respond before the RSVP deadline.";
    case "rsvp-deadline-passed":
      return "Online RSVP is now closed.";
    case "event-upcoming":
      return "The celebration is approaching.";
    case "event-today":
      return "Today is the celebration day.";
    case "event-in-progress":
      return "The celebration has begun.";
    case "event-completed":
      return "Thank you for celebrating with us.";
    case "post-event-gallery":
      return "Relive the celebration through the approved gallery.";
    case "site-archived":
      return "This celebration website is now archived.";
  }
}

/**
 * Security boundary:
 * The browser may display lifecycle guidance, but protected page access, RSVP
 * opening/closing, guest authorisation, gifting disclosure and post-event media
 * permissions must be enforced with a trusted server clock and server-side policy.
 */
