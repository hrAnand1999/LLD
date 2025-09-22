Problem Statement - 

Let's say we have to build a complex object, with so many parameters. What are the options do we have?
1. Pass all the parameters in the constructor, it might be possible that some parameter would be required or some not. 
2. Or if you don't want to pass all parameter in a single constructor, do constructor overloading. 
 Ex. House(window, wall)
     House(window, hall)
     House(floor, roof)
     But again this will have a problem, that compiler will understand constructor with 2 variables are similar and give compile time error.

✅ Builder Pattern Solution

1. Separates object construction from its representation
2. Allow step by step construction
3. Support method chaining for readability
4. Enable reuse of construction process for different object representations


Types of builder pattern - 
1. Simple builder
2. Director builder
3. Step Builder

1. Simple Builder - It is same which we discussed above

Disadvantage - 
    a. There is no surity of order, or lets say we want that before executing there must be body or there must be URL, but it is not possible as every method of builder will return it's object and we can run build over that.

2. Director builder pattern - Lets say there are some type of request which we are using too often, these request can be constructed via a function so whenever we call that function, all the work being done by that, like method chaining.

Disadvantage - 
    a. There is no surity of order, or lets say we want that before executing there must be body or there must be URL, but it is not possible as every method of builder will return it's object and we can run build over that.

3. Step Builder - In above 2 builder pattern, we can not say that when building something follow a particular path, means we can not put any constraint that only after using these methods you would be able to use the build function. For the same, this design pattern is being used. 
What it does special is it creates separate class for each required thing, and let's say B will be required after A, then after setting A, it return the object of B. 

Disadvantage - None

In python inheritance doesn't work properly, hence have to pass self.req in different class.
