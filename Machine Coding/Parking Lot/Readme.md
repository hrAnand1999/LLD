🅿️ Parking Lot – LLD Question
📌 Problem Statement

Design a Parking Lot System that can manage parking for different types of vehicles, track available spots, issue tickets, and calculate parking fees.

✅ Functional Requirements

The parking lot has multiple floors.

Each floor has multiple parking spots.

Parking spots are of different types:

Motorcycle

Car

Truck

Vehicles types:

Motorcycle

Car

Truck

A vehicle can be parked only in a compatible spot.

System should:

Assign a parking spot when a vehicle enters

Generate a parking ticket

Free the spot when the vehicle exits

Calculate parking fees based on time

System should show availability of spots per type.

❌ Non-Functional Requirements

Scalable (easy to add floors or spot types)

Thread-safe (multiple entry/exit points)

Extensible (pricing strategies, EV parking, etc.)

⚙️ Assumptions

One vehicle occupies one spot

Pricing is hourly

No reservations

Payment is done at exit
