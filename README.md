# Goals: automate a receipt ticket type and log information to a google sheet doc for backend administration.

1. Accept input data name and email 
    check if data is correct or return 
    ErrorValue: Please Enter correct name and or email.

2. Select type of massage  options: 1,2,3 from google sheet and Store it too google sheet 
    or Error value please select number 1-3

3. Select therapist: 
    Options 1,2,3. Dependent on type of massage selected.. i.e. Jared and Tor offer Sports massage not victoria as seen in wireframe
    or ErrorValue please select a number 1-3 


4. Return Clients name, email, therapist and type of therapy:
    
    Thank you {clients name} for choosing Love Massages. Your therapist {name of therapist} will be contacting you at {email} 
    to discuss your {type of massage} session.    

##   Testing
 * 7/5 Tested google doc is being read and data is printed in the console and it is.
  Inputs are returning data and printing a response.
   7/6 refraactored my code and chart and my code making use of a class booking
 


![wireframe concept](/assets/images/refractoredchart.png)
![wireframe Concept](/assets/images/wireframeupdate.png) 
