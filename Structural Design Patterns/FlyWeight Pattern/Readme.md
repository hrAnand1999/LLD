1. Definition

The Flyweight pattern is a structural design pattern that is used to minimize memory usage by sharing common data between multiple objects instead of storing duplicate copies.

It separates object state into:

Intrinsic state → shared, immutable data common across many objects.

Extrinsic state → unique data per object, supplied externally when needed.

👉 In short: Store shared stuff once, and reuse it everywhere.

2. Why/Where to Use It

Use Flyweight when:

You need a large number of objects (millions of them).

Many objects share common state/data (e.g., font, color, shape).

Memory footprint is a concern.

Without Flyweight, you might waste memory by duplicating the same data across objects.

3. How to Identify Situations

Ask yourself:

Do I have too many objects in memory?

Do these objects share a lot of identical data?

Can I externalize the small unique part of each object (extrinsic state)?

If yes → Flyweight may help.

4. Applications

Text editors: Each character object doesn’t store font, size, and style individually. Instead, a Flyweight stores font info once and characters reference it.

Game development: Large number of enemies, trees, bullets, or tiles → share common graphics data (sprite, texture) instead of duplicating.

Document rendering: Shapes, fonts, and formatting reused.

Data compression: Avoid duplicating repeated patterns.

=> use flyweight where we need to save RAM and have to create a lot of objects and these objects have something common called intrinsic properties.