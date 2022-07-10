""" 
Import section
"""
import os
import sys
from termcolor import colored
from pprint import pprint
import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_massages_pp3')

THERAPIES = ['Occupational Massage', 'Sports Massage', 'Rehabilitation Massage' ]
THERAPISTS = ['Jared', 'Tor', 'Victoria']


def welcome():
    """
    Introduction to the Application.
    """
    print(colored(('As a current member of love massages.\n'), 'cyan'))
    print(colored(('Enter your Name when prompted below:\n'), 'cyan'))
    print(colored(('Select your type of Massage Therapy \n'), 'cyan'))
    print(colored(('After that select your Massage Therapist.\n'), 'cyan'))
    print(colored(('Your booking will be made and you should see you confirmation.\n'), 'cyan'))

welcome()

class Booking:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def set_therapy(self, therapy):
        self.therapy_name = therapy_name

    def set_therapist(self, therapist):
        self.therapist_name = therapist_name    
# Customer Name
def customer_name():
    """
    The name_input function takes input from the user and stores it 
    in a variable that can be used further into the program
    """
   
    while True:
        customer_name = input("Please enter your name for a booking:\n").capitalize()
        if check_customer_name(customer_name):
            break
    print(f"\n Your Booking will be referenced using {customer_name}\n")
    return customer_name


def check_customer_name(customer_name):
    """
    Funtion checks if the customers name is longer 
    than 10 or not long enough. 
    """
    if len(customer_name) > 20:
        print('INVALID NAME. Too long')
        return False
    elif len(customer_name) == 0:
        print('Please enter your name')
    else:
        return True
    booking = Booking(customer_name)
    return booking
customer_name()

#Select your Therapy
def select_therapy_name():
    """
    The select_name_therapy function takes input from the user and stores it 
    in a variable that can be used further into the program
    """
    while True:
        print("\n Please select the type of Therapy you would like to receive. \n")
        print(THERAPIES)
   
        therapy_name = input("Please enter therapy:\n").capitalize()
        if check_therapy_name(therapy_name):
            break
    print(f"\n Your have chosen {therapy_name}\n")
    return therapy_name

def check_therapy_name(therapy_name):
    """
    Check if ther Therapy Chosen is Correct
    """
    if len(therapy_name) > 20:
        print('INVALID NAME. Too long')
        return False
    elif len(therapy_name) == 0:
        print('Please enter your name')
    else:
        return True
    booking = Booking(therapy_name)
    return booking
select_therapy_name()

#SelectTherapist
def select_therapist_name():
    """
    The select_name_therapy function takes input from the user and stores it 
    in a variable that can be used further into the program
    """
    while True:
        print("\n Your Therapist are: \n")        
        print(THERAPISTS)
   
        therapist_name = input("Please select your Therapist by entering ther name:\n").capitalize()
        if check_therapist_name(therapist_name):
            break
    print(f"\n Your have chosen {therapist_name}\n")
    return therapist_name

def check_therapist_name(therapist_name):
    """
    Check if the Therapist Chosen is Correctly
    """
    if len(therapist_name) > 20:
        print('INVALID THERAPIST')
        return False
    elif len(therapist_name) == 0:
        print('Please enter your name')
    else:
        return True
    booking = Booking(therapist_name)
    return booking
select_therapist_name()


# def save_booking(booking):
#     #make google sheet connection
#     #make google sheet call and save the data

# def main():
#     booking = get_customer_name()
#     booking = get_customer_phone_number()
#     select_therapy(booking)
#     select_therapist(booking)
#     save_booking(booking)

# selection = 1

# if not selection.isnumeric() or not (int(selection) < Therapies.length and int(selection) > 0)

# def getSelectedTherapy(selection):
#     return THERAPIES[selection-1]:

# main()