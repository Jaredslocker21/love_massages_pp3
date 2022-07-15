# Love Massages Internal Booking Application

### Love Massages is a simple internal booking application. Current members of Love Massages are offered Free Massages. 
### Their booking is referenced using their Name and is stored after all selection have been completed in the adminstrations cloud Google Document and can be contacted later on by their therapist to personally set up a date and time. 


![mock up of application](/assets/images/mockup.png)

# UX
### Purpose: 
1. Gives Loves Massages Administration a Booking application to share with their members. Store data from their user and directly updates to a Google Document where the administration can follow up with their members.

2. Allows current members to create their booking for a free massage by adding their name, selecting their type of Therapy. Their Therapist, and printing out a confirmation.

3. The user experience of the administration is to gather data from their current members. Name, therapy and therapist selections to create a booking for their members and back-end administration to follow up. 

To add function more Therapist's and Therapies can be added to the list's. Automatically adding them as a list item 1-4 or 5 or removing a list item will automatically shorten the displayed list.

# Flow chart of the program functions

![Flow Chart of the application](/assets/images/lucid_chart1.png)


# UI and Communication

## Colorful messages explaining their FREE MASSAGE and simple to follow instructions. 
## Organized with further coloring to comminicate selections and clarifications.

1. Welcome Message

![welcome message](/assets/images/welcomemessage.png)

2. Enter your name prompt. After your name has been entered. A colorful message is printed to validate the members selection and the next selection is prompted.


![Enter Name message](/assets/images/entername.png)    

3. Select Therapy:
 Select the type of Massage Therapy is a numerical selection: 1-4.
Both a numerical 1-4 selection and a press enter prompted
After the selection is made a confirmation of the selection is printed

![Select Therapy](/assets/images/selecttherapy.png)    


4. Select therapist: 
    Select the type of Massage Therapist is a numerical selection: 1-4.
    Both a numerical 1-4 selection and a press enter prompted.
    After the selection is made a confirmation of the selection is printed

![Select Therapist](/assets/images/selecttherapist.png)        


5. After every selection has been made a verification of the Clients name, therapy and therapist
    is printed back to the member and the booking is made in the google document for the backend administration.

![Thank You message](/assets/images/thankyoumessage.png)


6. A cloud  google document is then updated as per the function of the application.

![Google Document](/assets/images/google_cloud_document.png)


    


# Testing
 * 7/5 Tested google doc is being read and data is printed in the console and it is.
  Inputs are returning data and printing a response.

  * 7/15 Lauren-Nicole for testing the application and giving feedback.
 
![pep8 no errors](/assets/images/tests/pep_noerrors.png)


1. Name selection Test
* Nothing is entered and prompted to add a name

![Name Test](/assets/images/tests/test_empty_name.png)

* Numerical Test. When numbers are add a prompt to select letters fron A-Z and another request is made.

![Name Test](/assets/images/tests/test_empty_name.png)

* Over 20 character as I myself have a long name. I have chosed 20 characters.
    A too long prompt is given to the member and another request is made

![Name Test](/assets/images/tests/over_20char_test.png)

2. Choose Therapy Test.
* When letter is selected instead of number an invalid prompt occurs and another request is made to select 1-4.

![Therapy Selection Test](/assets/images/tests/invalid_therapy_choice.png)

* When a selection greater than the Therapies are offered another request is made to select 1-4.

![Therapy Selection Test](/assets/images/tests/select_therapy5_test.png)

* When nothing is selected an invalid prompt appears and another request is made to select 1-4.

3. Choose Therapist Test.

* When a selection greater than the Therapist are offered another request is made to select 1-4.

![Therapy Selection Test](/assets/images/tests/select_therapist5_test.png)

* When nothing is selected an ivalid prompt and another request is made to the member.

![Therapy Selection Test](/assets/images/tests/therapist_nothing_selected.png)


# Frameworks: Libraries & Programs Used
GitPod - to create application in a cloud environment
GitHub - to store my repository .
Lucid - Create a flow chart.
Heroku - Deployment for a python application evironment.
VS studio code to edit and store saved editable code.

# Deployment

log in to heroku
create a new app
navigate to settings
add the following KEY/VALUE pairs:
CREDS + copy/paste data from creds.json file
PORT + 8000
add build packs (in this order)
Python
nodejs
go to GitPod terminal
type the following commands into the terminal:
heroku login -i
enter in username + password
heroku apps
heroku git:remote -a my-app-name
git add .
git commit -m "Deploy to Heroku cia CLI"
git push origin main
git push heroku main

# Credits

[StackOverflow](https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops) provided the reminder for how to index my 'for loop'.

[Programiz](https://www.programiz.com/python-programming/methods/string/isnumeric) Numeric validations

[Programiz](https://www.programiz.com/python-programming/methods/string/isalpha) Alphabet validations

[Programiz](https://www.programiz.com/python-programming/methods/string/isalpha) Inumerate method for displaying lists

[Stack Overflow](https://stackoverflow.com/questions/40275866/pycharm-shows-pep8-expected-2-blank-lines-found-1) blank lines

Instructions on adding (Termcolor)[https://pypi.org/project/termcolor/] came from [StackOverflow](https://stackoverflow.com/questions/51530437/no-module-named-termcolor).


I want to thank my fellow student Lauren-Nicole for testing and Al-Amin Sanusi for keeping my head cool. 

My mentor Akshat Garg for his patience, clarity and just overall awesome attitude.
















