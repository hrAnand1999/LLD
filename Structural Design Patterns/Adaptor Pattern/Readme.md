Problem Statement - 
Lets say we are taking data from stock exchange in xml format and we have built a dashboard over that. Now we want to use this data for analytics purpose as well, for the same we have taken subscription for 3rd party like moengage or something, but the catch is they are accepting data only in json format. Now we have 2 option, either change the code of moengage to accept XML data or send the json the data. 

Solution - 
We don't want to make any changes in our existing code of dashboard, as it will violate the SOLID principle, so we created a 3rd service name integration service, which will handle all the integration related to 3rd parties. Now what it will do is it will convert the data type from xml to json and make it compatible. 


Applications - 
1. whenever we have to integrate 3rd party library with our codebase
2. Whenever we have to build something around legacy codebase, and there are difference b/w data required in microservice and data presented by legacy codebase
3. Normal API response, where we take data from db and convert it according to the requirement of the user