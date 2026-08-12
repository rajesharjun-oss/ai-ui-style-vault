/**
 * Framework-neutral reference types for Fast-Casual Commerce.
 * Money is represented in minor units to avoid floating-point errors.
 * Adapt these contracts to the target backend; do not treat sample data as production truth.
 */

export type CurrencyCode = string;
export type ISODateTime = string;
export type BranchId = string;
export type ProductId = string;
export type CartLineId = string;
export type OptionGroupId = string;
export type OptionValueId = string;

export interface Money {
  amountMinor: number;
  currency: CurrencyCode;
}

export type FulfilmentMode = "delivery" | "pickup" | "dine-in" | "takeaway";

export type AvailabilityState =
  | "available"
  | "limited"
  | "out-of-stock"
  | "temporarily-unavailable"
  | "store-closed"
  | "service-unavailable";

export interface OpeningWindow {
  dayOfWeek: 0 | 1 | 2 | 3 | 4 | 5 | 6;
  opensAt: string;
  closesAt: string;
  fulfilmentModes?: FulfilmentMode[];
}

export interface Branch {
  id: BranchId;
  name: string;
  address: string;
  latitude?: number;
  longitude?: number;
  timezone: string;
  phone?: string;
  fulfilmentModes: FulfilmentMode[];
  openingWindows: OpeningWindow[];
  statusSource: "live" | "schedule" | "manual" | "unknown";
}

export interface Category {
  id: string;
  name: string;
  description?: string;
  sortOrder: number;
  productIds: ProductId[];
}

export interface ProductImage {
  src: string;
  width: number;
  height: number;
  alt: string;
  provenance: "owner-provided" | "original" | "generated-concept" | "licensed";
}

export interface OptionValue {
  id: OptionValueId;
  name: string;
  description?: string;
  priceDelta: Money;
  availability: AvailabilityState;
  dietaryTags?: string[];
  allergenIds?: string[];
  sortOrder: number;
}

export interface OptionGroup {
  id: OptionGroupId;
  name: string;
  description?: string;
  required: boolean;
  selection: "single" | "multiple";
  minimumSelections: number;
  maximumSelections: number;
  values: OptionValue[];
  sortOrder: number;
}

export interface Product {
  id: ProductId;
  categoryId: string;
  name: string;
  description: string;
  basePrice: Money;
  priceLabel: "fixed" | "from";
  availability: AvailabilityState;
  images: ProductImage[];
  optionGroups: OptionGroup[];
  dietaryTags?: string[];
  allergenIds?: string[];
  branchIds?: BranchId[];
  sortOrder: number;
}

export interface SelectedOptionGroup {
  groupId: OptionGroupId;
  valueIds: OptionValueId[];
}

export interface ProductConfiguration {
  selectedGroups: SelectedOptionGroup[];
  specialInstructions?: string;
}

export interface CartLine {
  id: CartLineId;
  productId: ProductId;
  productName: string;
  configuration: ProductConfiguration;
  quantity: number;
  unitPrice: Money;
  lineTotal: Money;
  availability: AvailabilityState;
  conflictCodes: CommerceConflictCode[];
}

export type CommerceConflictCode =
  | "PRODUCT_UNAVAILABLE"
  | "OPTION_UNAVAILABLE"
  | "REQUIRED_OPTION_MISSING"
  | "BRANCH_UNAVAILABLE"
  | "FULFILMENT_UNAVAILABLE"
  | "PRICE_CHANGED"
  | "MINIMUM_ORDER_NOT_MET";

export interface PromotionAdjustment {
  id: string;
  name: string;
  amount: Money;
  code?: string;
  qualificationText?: string;
}

export interface FeeLine {
  id: string;
  name: string;
  amount: Money;
  verified: boolean;
}

export interface CartContext {
  branchId: BranchId;
  fulfilmentMode: FulfilmentMode;
  addressId?: string;
  scheduledFor?: ISODateTime;
}

export interface Cart {
  id: string;
  context: CartContext;
  lines: CartLine[];
  promotions: PromotionAdjustment[];
  fees: FeeLine[];
  subtotal: Money;
  discountTotal: Money;
  feeTotal: Money;
  taxTotal?: Money;
  total: Money;
  conflictCodes: CommerceConflictCode[];
  verifiedAt?: ISODateTime;
}

export interface DeliveryEligibility {
  state: "idle" | "validating" | "eligible" | "outside-zone" | "unavailable" | "error";
  branchId?: BranchId;
  fee?: Money;
  minimumOrder?: Money;
  reason?: string;
  verifiedAt?: ISODateTime;
}

export type PaymentState =
  | "idle"
  | "submitting"
  | "pending"
  | "authorised"
  | "failed"
  | "cancelled";

export type OrderStatus =
  | "confirmation-pending"
  | "confirmed"
  | "preparing"
  | "ready-for-pickup"
  | "out-for-delivery"
  | "delivered"
  | "delayed"
  | "cancelled";

export interface OrderStatusEvent {
  status: OrderStatus;
  occurredAt?: ISODateTime;
  label: string;
  description?: string;
  verified: boolean;
}

export interface Order {
  id: string;
  publicIdentifier: string;
  branchId: BranchId;
  fulfilmentMode: FulfilmentMode;
  status: OrderStatus;
  statusEvents: OrderStatusEvent[];
  lines: CartLine[];
  total: Money;
  customerContact: string;
  addressLabel?: string;
  pickupInstructions?: string;
  estimatedAt?: ISODateTime;
  createdAt: ISODateTime;
}

export interface CommerceDataSourceContract {
  branches: "api" | "cms" | "static-prototype";
  menu: "api" | "cms" | "static-prototype";
  availability: "api" | "manual" | "static-prototype";
  pricing: "api" | "cms" | "static-prototype";
  promotions: "api" | "cms" | "unsupported" | "static-prototype";
  loyalty: "api" | "unsupported" | "static-prototype";
  payments: "provider" | "unsupported" | "static-prototype";
  orders: "api" | "unsupported" | "static-prototype";
  tracking: "api" | "unsupported" | "static-prototype";
}
