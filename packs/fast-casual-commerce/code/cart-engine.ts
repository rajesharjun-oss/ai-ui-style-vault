import type {
  Cart,
  CartLine,
  CommerceConflictCode,
  FeeLine,
  Money,
  OptionGroup,
  Product,
  ProductConfiguration,
  PromotionAdjustment,
  SelectedOptionGroup,
} from "./commerce-types";

/** Pure reference functions. Production systems must revalidate all totals server-side. */

export class CommerceValidationError extends Error {
  readonly codes: CommerceConflictCode[];

  constructor(message: string, codes: CommerceConflictCode[]) {
    super(message);
    this.name = "CommerceValidationError";
    this.codes = codes;
  }
}

export function assertSameCurrency(values: Money[]): string {
  const currencies = new Set(values.map((value) => value.currency));
  if (currencies.size !== 1) {
    throw new CommerceValidationError("Currency mismatch in commerce calculation.", ["PRICE_CHANGED"]);
  }
  return values[0]?.currency ?? "";
}

export function money(amountMinor: number, currency: string): Money {
  if (!Number.isInteger(amountMinor)) {
    throw new TypeError("Money amountMinor must be an integer.");
  }
  return { amountMinor, currency };
}

export function addMoney(values: Money[], fallbackCurrency: string): Money {
  if (values.length === 0) return money(0, fallbackCurrency);
  const currency = assertSameCurrency(values);
  return money(values.reduce((total, value) => total + value.amountMinor, 0), currency);
}

export function multiplyMoney(value: Money, quantity: number): Money {
  if (!Number.isInteger(quantity) || quantity < 0) {
    throw new RangeError("Quantity must be a non-negative integer.");
  }
  return money(value.amountMinor * quantity, value.currency);
}

function selectedForGroup(
  configuration: ProductConfiguration,
  groupId: string,
): SelectedOptionGroup | undefined {
  return configuration.selectedGroups.find((selection) => selection.groupId === groupId);
}

function validateGroup(group: OptionGroup, selection?: SelectedOptionGroup): CommerceConflictCode[] {
  const selectedIds = new Set(selection?.valueIds ?? []);
  const conflicts: CommerceConflictCode[] = [];

  if (group.required && selectedIds.size < Math.max(1, group.minimumSelections)) {
    conflicts.push("REQUIRED_OPTION_MISSING");
  }

  if (selectedIds.size < group.minimumSelections || selectedIds.size > group.maximumSelections) {
    conflicts.push("REQUIRED_OPTION_MISSING");
  }

  if (group.selection === "single" && selectedIds.size > 1) {
    conflicts.push("REQUIRED_OPTION_MISSING");
  }

  for (const selectedId of selectedIds) {
    const value = group.values.find((candidate) => candidate.id === selectedId);
    if (!value || value.availability !== "available") {
      conflicts.push("OPTION_UNAVAILABLE");
    }
  }

  return [...new Set(conflicts)];
}

export function validateConfiguration(
  product: Product,
  configuration: ProductConfiguration,
): CommerceConflictCode[] {
  const conflicts: CommerceConflictCode[] = [];

  if (product.availability !== "available" && product.availability !== "limited") {
    conflicts.push("PRODUCT_UNAVAILABLE");
  }

  for (const group of product.optionGroups) {
    conflicts.push(...validateGroup(group, selectedForGroup(configuration, group.id)));
  }

  const knownGroupIds = new Set(product.optionGroups.map((group) => group.id));
  if (configuration.selectedGroups.some((selection) => !knownGroupIds.has(selection.groupId))) {
    conflicts.push("OPTION_UNAVAILABLE");
  }

  return [...new Set(conflicts)];
}

export function calculateConfiguredUnitPrice(
  product: Product,
  configuration: ProductConfiguration,
): Money {
  const conflicts = validateConfiguration(product, configuration);
  if (conflicts.length > 0) {
    throw new CommerceValidationError("Product configuration is not purchasable.", conflicts);
  }

  const adjustments: Money[] = [product.basePrice];

  for (const group of product.optionGroups) {
    const selectedIds = new Set(selectedForGroup(configuration, group.id)?.valueIds ?? []);
    for (const value of group.values) {
      if (selectedIds.has(value.id)) adjustments.push(value.priceDelta);
    }
  }

  return addMoney(adjustments, product.basePrice.currency);
}

export function buildCartLine(params: {
  id: string;
  product: Product;
  configuration: ProductConfiguration;
  quantity: number;
}): CartLine {
  const { id, product, configuration, quantity } = params;
  if (!Number.isInteger(quantity) || quantity < 1) {
    throw new RangeError("Cart-line quantity must be an integer of at least one.");
  }

  const conflicts = validateConfiguration(product, configuration);
  if (conflicts.length > 0) {
    throw new CommerceValidationError("Cannot add invalid product configuration.", conflicts);
  }

  const unitPrice = calculateConfiguredUnitPrice(product, configuration);
  return {
    id,
    productId: product.id,
    productName: product.name,
    configuration,
    quantity,
    unitPrice,
    lineTotal: multiplyMoney(unitPrice, quantity),
    availability: product.availability,
    conflictCodes: [],
  };
}

function normaliseNegativeAdjustment(adjustment: PromotionAdjustment): Money {
  return money(-Math.abs(adjustment.amount.amountMinor), adjustment.amount.currency);
}

export function calculateCartTotals(params: {
  cart: Omit<Cart, "subtotal" | "discountTotal" | "feeTotal" | "total" | "conflictCodes">;
  minimumOrder?: Money;
}): Cart {
  const { cart, minimumOrder } = params;
  const currency =
    cart.lines[0]?.lineTotal.currency ??
    cart.promotions[0]?.amount.currency ??
    cart.fees[0]?.amount.currency ??
    minimumOrder?.currency ??
    "NGN";

  const subtotal = addMoney(cart.lines.map((line) => line.lineTotal), currency);
  const discountTotal = addMoney(
    cart.promotions.map(normaliseNegativeAdjustment),
    currency,
  );
  const feeTotal = addMoney(cart.fees.map((fee: FeeLine) => fee.amount), currency);
  const taxTotal = cart.taxTotal ?? money(0, currency);
  const total = addMoney([subtotal, discountTotal, feeTotal, taxTotal], currency);

  const conflictCodes = new Set<CommerceConflictCode>(
    cart.lines.flatMap((line) => line.conflictCodes),
  );

  if (minimumOrder) {
    assertSameCurrency([subtotal, minimumOrder]);
    if (subtotal.amountMinor < minimumOrder.amountMinor) {
      conflictCodes.add("MINIMUM_ORDER_NOT_MET");
    }
  }

  return {
    ...cart,
    subtotal,
    discountTotal,
    feeTotal,
    taxTotal,
    total,
    conflictCodes: [...conflictCodes],
  };
}

export function updateLineQuantity(line: CartLine, quantity: number): CartLine | null {
  if (!Number.isInteger(quantity) || quantity < 0) {
    throw new RangeError("Quantity must be a non-negative integer.");
  }
  if (quantity === 0) return null;
  return {
    ...line,
    quantity,
    lineTotal: multiplyMoney(line.unitPrice, quantity),
  };
}

export function replaceLineConflicts(
  line: CartLine,
  conflicts: CommerceConflictCode[],
): CartLine {
  return { ...line, conflictCodes: [...new Set(conflicts)] };
}

export function describeCartRecalculation(before: Cart, after: Cart): string[] {
  const changes: string[] = [];
  const beforeLines = new Map(before.lines.map((line) => [line.id, line]));

  for (const afterLine of after.lines) {
    const beforeLine = beforeLines.get(afterLine.id);
    if (!beforeLine) {
      changes.push(`${afterLine.productName} was added.`);
      continue;
    }
    if (beforeLine.lineTotal.amountMinor !== afterLine.lineTotal.amountMinor) {
      changes.push(`${afterLine.productName} price changed.`);
    }
    if (beforeLine.quantity !== afterLine.quantity) {
      changes.push(`${afterLine.productName} quantity changed.`);
    }
    if (beforeLine.conflictCodes.join("|") !== afterLine.conflictCodes.join("|")) {
      changes.push(`${afterLine.productName} availability or configuration changed.`);
    }
    beforeLines.delete(afterLine.id);
  }

  for (const removed of beforeLines.values()) {
    changes.push(`${removed.productName} is no longer in the cart.`);
  }

  if (before.feeTotal.amountMinor !== after.feeTotal.amountMinor) changes.push("Fees changed.");
  if (before.discountTotal.amountMinor !== after.discountTotal.amountMinor) changes.push("Discount changed.");
  if (before.total.amountMinor !== after.total.amountMinor) changes.push("Order total changed.");

  return changes;
}

export function canCheckout(cart: Cart): boolean {
  return cart.lines.length > 0 && cart.conflictCodes.length === 0 && cart.total.amountMinor >= 0;
}

/**
 * Security boundary:
 * The browser calculation is presentation only. The server must reprice and revalidate
 * branch, fulfilment, address, availability, promotions, fees, tax, payment, and order
 * creation with an idempotency key before accepting an order. A payment-pending state
 * must be resolved through the payment or order API; never infer confirmation client-side.
 */
