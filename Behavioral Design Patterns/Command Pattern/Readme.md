🔹 What is the Command Pattern?

The Command pattern turns a request into a standalone object.
It encapsulates what action to perform, who will perform it, and parameters.
The requester (invoker) doesn’t need to know the actual implementation of the action.

👉 In simple words: It’s a way to decouple the object that invokes an operation from the one that knows how to perform it.


🔹 Structure
Client: Creates command and sets the receiver.
Command: Interface with execute() method.
ConcreteCommand: Implements command, calls receiver methods.
Receiver: Does the actual work.
Invoker: Stores and triggers commands.



🔹 When to Use It?

You should consider Command Pattern when:
You need to parameterize objects with operations (like scheduling tasks).
You need to support undo/redo.
You need to queue, log, or store requests.
You want to decouple sender from receiver.

🔹 Real-World Use Cases

GUI applications (button clicks → commands).
Text editor (undo/redo actions).
Job queues (execute later).
Remote controls (turn TV on/off, change channel).
Macro recording (store commands and replay).