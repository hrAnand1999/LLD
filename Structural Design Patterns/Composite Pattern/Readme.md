Problem Statement - 
In many applications, we deal with hierarchical system. tree like structure
    - some are leaf nodes
    - some are composite element of multiple nodes.
Without a uniform interface we need to solve both the logics separately, which lead to repetitive code.

Solution - 
We create a uniform interface and treat both leaf and composite node as same.

Notes - 
Very specific use case

Definition - 
Composite Pattern composes object into tree like structure, representing a part whole hierarchy. It let client treats individual object and composition of object uniformly.

Applications - 

1. File  system
2. Where we have to solve tree like structure, means there are nested objects.