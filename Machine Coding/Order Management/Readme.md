📦 Order Management System (OMS) — LLD Interview Question (SDE-2)
📌 Problem Statement

Design an Order Management System that manages the complete lifecycle of an order, starting from browsing inventory and adding items to cart, through order placement, payment processing, and fulfillment, while ensuring consistency and scalability.

✅ Functional Requirements

Inventory & Cart

    A user can view items available in inventory along with available quantities.

    A user can add items to a cart, only if sufficient inventory is available.

    The cart supports:

        Adding items

        Updating quantities

        Removing items

Order Management

    A user can place an order with one or more items from the cart.

    Before order creation, the system must validate availability for all items.

    Inventory should be reserved at order creation to prevent over-selling.

    Each order maintains the following states:

        CREATED

        CONFIRMED

        PAID

        SHIPPED

        DELIVERED

        CANCELLED

Order Details

    Each order contains:

    Order ID

    List of order items

    Total amount

    Order status

    Creation and update timestamps

Payment & Fulfillment

    Payment must be successfully completed before shipping.

    Orders can be cancelled only before shipping.

    Inventory must be released on order cancellation.

    System should support partial order cancellation (optional).

User Operations

    User should be able to:

    View order details

    Track order status

    Cancel eligible orders

❌ Non-Functional Requirements

    Strong consistency to prevent over-selling.

    Scalability to support high order volume.

    Idempotency for order creation and payment APIs.

    Fault tolerance to handle partial failures.

    Extensibility to support refunds, promotions, and returns.

⚙️ Assumptions

    Single currency.

    Single warehouse (multi-warehouse is out of scope).

    Payment is synchronous.

    Inventory reservation happens at order creation.

    No discounts or promotions (can be added later).