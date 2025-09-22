Use Case

1. When we want to use different variants of algorithm within an object and be able to switch in runtime. 

2. When child class have same code but parent don't have.

3. Use it when class has a massive if else block of code that switches between different variants during runtime.

4. It also follows Open for extension and Closed for modification principle.


Example => Lets say we have to build payment system with different payment options and more payment options can be added in future. Each method of payment have separate core logic of processing. So there would be a context and the value which customer will pass will help context to choose the payment object.
