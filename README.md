Googleappengine
===============
The site I designed will compute the factorial of the entered number and displays output along with the time taken for computation. Users can use this service by logging in with their google account which is a part of the google app engine webservice Google user management.

I used python language for writing the code.

Here is an example describing its functionality

Eg : Enter your number: 5 output: Factorial of 5 is : 120 Time: 0.0149900913239

The two Google App Engine webservices that I used for my application are

a.) Memcache which stores the factorial for the entered numbers and when those numbers are re entered delay for displaying output will be very less and we can see this from the time function which I used for better understanding. Users can even flush the memcache by entering &f in the url.

b.) Google User Managment: This service verifies the user identity before he/she can use the application.Users can login and logout after they use the application
