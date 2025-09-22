🧩 Bridge Design Pattern — Problem Statement It Solves

The Bridge pattern solves the problem of tight coupling between an abstraction and its implementation, especially when both need to evolve independently.

🔧 Problem in Detail
In traditional object-oriented design, you might have a class hierarchy like this:

Shape
├── Circle
├── Square
Now suppose you want to support multiple color shapes (e.g., red, blue). You might end up with:

RedCircle
BlueCircle
RedSquare
BlueSquare
This leads to a combinatorial explosion of classes — every new shape × every new color = a new class.

If there are 4 shapes and 4 colors, it will lead to 16 classes, i.e n * m classes.

✅ How Bridge Solves It
The Bridge pattern splits the hierarchy into two orthogonal dimensions:

1. Abstraction (e.g., Shape)
2. Implementation (e.g., Color)
Now you can mix and match them without creating new subclasses for every combination.

🔍 How to Identify When to Use Bridge
Ask yourself:

1. Do I have two dimensions that vary independently?
2. Is my class hierarchy growing too large due to combinations?
3. Do I want to change implementations at runtime or independently?
If yes, Bridge is likely the right choice.


Difference b/w bridge and strategy => Intent of the problem which we are solving