/**
 * Framework-neutral reference contracts for celebration and couple microsites.
 * These types are guidance. Production systems must enforce privacy, guest
 * authorization, RSVP limits and lifecycle transitions on the server.
 */

export type ISODateTime = string;
export type IANATimeZone = string;
export type EventId = string;
export type GuestId = string;
export type MediaId = string;

export type EventType =
  | "wedding"
  | "nikkah"
  | "engagement"
  | "anniversary"
  | "birthday"
  | "graduation"
  | "memorial"
  | "private-celebration"
  | "multi-event-celebration";

export type EventLifecycleState =
  | "save-the-date"
  | "invitation-announced"
  | "rsvp-not-open"
  | "rsvp-open"
  | "rsvp-deadline-passed"
  | "event-upcoming"
  | "event-today"
  | "event-in-progress"
  | "event-completed"
  | "post-event-gallery"
  | "site-archived";

export type PrivacyModel =
  | "public"
  | "public-summary-private-details"
  | "guest-code"
  | "authenticated-guest"
  | "fully-private";

export type CapabilityStatus =
  | "verified-and-integrated"
  | "design-only-prototype"
  | "requires-integration"
  | "requires-host-confirmation"
  | "out-of-scope";

export type ContentStatus =
  | "verified-couple-content"
  | "requires-couple-confirmation"
  | "private-do-not-index"
  | "prototype-only";

export interface CelebrationMeta {
  id: string;
  title: string;
  eventType: EventType;
  timezone: IANATimeZone;
  locale: string;
  fictional: boolean;
}

export interface HostProfile {
  id: string;
  displayName: string;
  preferredTitle?: string;
  shortBio?: string;
  fullBio?: string;
  quotation?: string;
  portraitMediaId?: MediaId;
  contentStatus: ContentStatus;
  quickFacts: Array<{
    label: string;
    value: string;
    private?: boolean;
  }>;
}

export interface CelebrationEvent {
  id: EventId;
  name: string;
  type: string;
  startsAt: ISODateTime;
  endsAt: ISODateTime;
  timezone: IANATimeZone;
  venue?: string;
  address?: string;
  directionsUrl?: string;
  attendanceScope: "all-invited-guests" | "invitation-specific" | "private-family" | "public";
  confirmationStatus: "confirmed" | "provisional" | "cancelled";
  instructions?: string;
}

export interface LifecycleConfiguration {
  saveTheDateAt?: ISODateTime;
  invitationAnnouncedAt?: ISODateTime;
  rsvpOpensAt?: ISODateTime;
  rsvpClosesAt?: ISODateTime;
  primaryEventStart: ISODateTime;
  primaryEventEnd: ISODateTime;
  postEventPublishAt?: ISODateTime;
  archiveAt?: ISODateTime;
  timezone: IANATimeZone;
  postEventMode: "thank-you" | "gallery" | "read-only-archive" | "retire-site";
}

export interface GuestInvitation {
  guestId: GuestId;
  householdId?: string;
  displayName: string;
  invitedEventIds: EventId[];
  approvedGuestLimit: number;
  canEditBeforeDeadline: boolean;
  status: "active" | "revoked" | "used";
}

export type AttendanceResponse = "attending" | "not-attending" | "partial";

export interface AttendeeResponse {
  displayName: string;
  invitationRole: "primary" | "named-guest" | "approved-plus-one" | "child";
  mealPreference?: string;
  dietaryRequirements?: string;
}

export interface RSVPSubmission {
  eventId: string;
  guestId: GuestId;
  attendance: AttendanceResponse;
  selectedEventIds: EventId[];
  attendees: AttendeeResponse[];
  message?: string;
  revision: number;
  submittedAt: ISODateTime;
  privacyNoticeAccepted: true;
}

export interface RSVPConfirmation {
  reference: string;
  guestId: GuestId;
  attendance: AttendanceResponse;
  selectedEventIds: EventId[];
  attendeeCount: number;
  confirmedAt: ISODateTime;
  revision: number;
  deliveryStatus?: "onscreen" | "pending" | "sent" | "failed";
}

export interface MediaAsset {
  id: MediaId;
  type: "image" | "video" | "audio" | "document";
  src: string;
  poster?: string;
  alt?: string;
  caption?: string;
  transcript?: string;
  provenance:
    | "couple-provided"
    | "host-provided"
    | "photographer-licensed"
    | "licensed-third-party"
    | "decorative-generated-asset"
    | "original";
  access: "public" | "guest-only" | "host-only";
  consentStatus: "confirmed" | "pending" | "restricted";
  downloadAllowed: boolean;
}

export interface GuestAccessContext {
  privacyModel: PrivacyModel;
  authenticated: boolean;
  guestId?: GuestId;
  householdId?: string;
  authorisedEventIds: EventId[];
  mediaAccess: Array<"public" | "guest-only" | "host-only">;
}

export interface IntegrationContract {
  guestLookup: CapabilityStatus;
  rsvpPersistence: CapabilityStatus;
  emailConfirmation: CapabilityStatus;
  messagingConfirmation: CapabilityStatus;
  maps: CapabilityStatus;
  calendar: CapabilityStatus;
  mediaHosting: CapabilityStatus;
  guestUploads: CapabilityStatus;
  registry: CapabilityStatus;
  protectedGifting: CapabilityStatus;
  analytics: CapabilityStatus;
}

export interface CelebrationSiteContract {
  meta: CelebrationMeta;
  hosts: HostProfile[];
  events: CelebrationEvent[];
  lifecycle: LifecycleConfiguration;
  privacyModel: PrivacyModel;
  integrations: IntegrationContract;
  media: MediaAsset[];
}
