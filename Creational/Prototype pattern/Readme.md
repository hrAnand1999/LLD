🧩 Problem Statement It Solves
Creating new objects can be costly or complex, especially when:
1. Object creation involves a lot of configuration.
2. Objects are resource-intensive to instantiate.
3. You need many similar objects with slight variations.

Prototype pattern solves this by allowing you to clone existing objects instead of creating new ones from scratch.

✅ Use Cases
1. When object creation is expensive (e.g., database connections, network calls).
2. When you need to create many similar objects.
3. When system performance is critical and object creation time must be minimized.
4. When objects are created at runtime and you want to avoid subclassing.

🛠️ Applications
1. Game development: Cloning enemies or items with similar properties.
2. Document editors: Duplicating elements like shapes or text boxes.
3. UI frameworks: Copying widgets with predefined styles.
4. Machine learning: Cloning models with similar configurations.