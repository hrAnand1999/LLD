Problem Statement :- 
We have to separate out the data sotrage logic and traversal logic to maintain the single responsibility principle.

Lets say we have a playlist of song class which currently uses vector to store songs, but in future lets say we have to switch to linked list then we have to change the traversal logic as well. Thats why we use iterators.