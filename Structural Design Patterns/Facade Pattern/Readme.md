Problem Statement - 
Let's say I've opened a comapny and now I want to receive payments, one option is I will deal will with all the banking mess and integrate all and take permissions. Other is that I can simply use razorpay to integrate for all our payment need and all the necessity permission have already been taken by them. 
In short facade design pattern decouples the client from system. And make it very easy for client to interact with a complex system by providing only the necessary function required by the client.

A -> B -> C
=> This design pattern tell about principle of least knowledge, i.e. A should only know about B, A can not call any method of C, if A has to do any anything from C, it should go via B.

Facade Vs Adapter

Facade design pattern hides the complexity. Whereas Adapter design pattern helps in communication of 2 different interfaces.

UseCase - 
1. Lets say paytm is providing upi payment by simply entering the pin and clicking ok, but internally there are a lot of systems like NPCI, bank, whose class/function are also being called.