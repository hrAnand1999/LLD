🧩 What is the Decorator Pattern?
The Decorator Pattern is a design pattern used to add new behavior to objects dynamically without changing their structure. It’s like wrapping an object with another object that adds something new.

Think of it like putting a gift in a box, then wrapping it in fancy paper. The gift is still the same, but now it looks cooler!


🎯 What Problem Does It Solve?
It solves the problem of extending functionality without:
    ->modifying existing code (which might be risky or not allowed),
    ->creating lots of subclasses (which can get messy).


🧰 Use Case
1) Imagine you have a basic notification system. You want to add features like:

->sending email,
->sending SMS,
->logging the notification.
Instead of modifying the original class or creating many subclasses, you can decorate the notification with these features.

2) Coffee Shop with base coffee and lot of toppings & find their cost. If we create class for each combination of toppings and base coffee, there would be a lot of classes.

3) Pizza shop with base pizza & lot of toppings & find their cost.

4) Lets say we have payment processor class in a legacy system, it is being used across the org for processing payments. Now for our use case we want to add logging and security code in it. 
Can we modify the existing code => No, bcz then we need to test at all the places where this function is being used.
Can we extend from this class and create one for our use case ? => Ofcourse yes

