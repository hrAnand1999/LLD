📦 LLD Problem: Food Delivery Platform (Swiggy/Zomato-like)
🧠 Context

Design a food delivery system that allows users to browse restaurants, explore food items, place orders, and track delivery. The system should be extensible, maintainable, and scalable.

You are not required to build UI or networking. Focus on object modeling, interactions, and core business logic.

🔹 Part 1: Location & User Management (LLD – Core Modeling)
Requirements

The system supports multiple districts.

Each user belongs to exactly one district.

Each restaurant operates in exactly one district.

A user can only see restaurants available in their own district.

Expectations from Candidate

Design classes for:

User

District

Decide:

How district information is stored

How users are mapped to districts

Discuss:

How future expansion to multi-district delivery could be supported

🔹 Part 2: Restaurant Management (LLD – Aggregates & Filtering)
Requirements

Each restaurant:

Has a unique ID

Belongs to a district

Has a user rating (double: 1.0–5.0)

Serves veg, non-veg, or both

Users can:

View all restaurants in their district

Sort restaurants by rating (ascending/descending)

Expectations

Model:

Restaurant

RestaurantService / Repository

Think about:

Sorting strategies

Where rating logic should live

Discuss:

How ratings could be updated dynamically

🔹 Part 3: Food Item & Menu Design (LLD – Composition)
Requirements

Each restaurant has a menu containing multiple food items.

Each food item:

Has name, price

Is veg or non-veg

Has its own user rating

Users can:

View restaurant menu

Sort food items by rating

Filter food by veg / non-veg

Expectations

Design:

FoodItem

Menu

Handle:

Filtering logic

Sorting logic

Discuss:

Should food rating be independent or derived?

🔹 Part 4: Cart Design (Machine Coding Focus)
Requirements

A user can add multiple food items to a cart.

Items can belong to different restaurants.

Cart should support:

Add item

Remove item

Update quantity

View cart summary (total price)

Constraints

No inventory limits for now

No restaurant-wise cart restriction

Expectations

Design:

Cart

CartItem

Implement:

Core cart operations

Handle edge cases:

Duplicate items

Empty cart

🔹 Part 5: Order Creation & Lifecycle (LLD – State Machine)
Requirements

User can place an order from the cart.

Order contains:

Order ID

User

List of food items

Total amount

Order status

Order Status Flow
CREATED → CONFIRMED → PAID → OUT_FOR_DELIVERY → DELIVERED
                    ↘ CANCELLED

Expectations

Model:

Order

OrderStatus (enum)

Design:

Valid state transitions

Discuss:

How invalid transitions are prevented

🔹 Part 6: Payment Design (LLD – Strategy Pattern)
Requirements

User can choose payment mode:

UPI

Card

Cash on Delivery

Payment happens during order placement.

Order moves to PAID only after successful payment.

Expectations

Design:

Payment interface

Concrete payment implementations

Apply:

Strategy pattern

Discuss:

How to add new payment methods later

🔹 Part 7: Order Tracking & History (LLD – Querying & Read Models)
Requirements

User can:

Track current order status

View list of past orders

Order status updates should be visible immediately.

Expectations

Design:

OrderService

Handle:

Order storage

Retrieval by user

Discuss:

In-memory vs persistent storage

🔹 Part 8: Non-Functional Expectations (Discussion)

Ask the candidate to briefly discuss:

How to make this system:

Scalable

Thread-safe

How ratings could be:

Averaged

Updated concurrently

How this design can support:

Discounts

Restaurant availability

Delivery partners (future)
