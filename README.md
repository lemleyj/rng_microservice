# rng_microservice
A microservice that generates and returns a random number or object to the user depending on what was received from the client. 

TO USE: 
 - if provided with a blank string, the server will return a random number between 0-10000.
 - if provided with a range as a tuple [i.e. (0, 10)], the server will return a random number between provided range.
 - if provided with a list of objects (i.e. [111, 222, 333]), the server will return a random object from the list.

 UML Diagram: 

![Screenshot](rng_microservice_uml.png)
