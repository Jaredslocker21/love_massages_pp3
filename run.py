""" 
Import section
"""
import os
import sys
from termcolor import colored
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
    print(colored(('Welcome to Love Massages.\n'), 'cyan'))
    print(colored(('Enter your Name and your Email address when prompted below:\n'), 'cyan'))
    print(colored(('Select your type of Massage Therapy \n'), 'cyan'))
    print(colored(('After that select your Massage Therapist.\n'), 'cyan'))
    print(colored(('Your booking will be made and you should see you confirmation.\n'), 'cyan'))

welcome()

class Booking:
    def __init__(self, therapy):
        self.customer_name = customer_name

    def set_email(self, email):
        self.email = email 

    def set_therapy(self, therapy):
        self.therapy = therapy

    def set_therapist(self, therapist):
        self.therapist = therapist    

def get_customer_name():
    """ 
    Get the customer name, validate the the input create the booking
    """
    #customer input
    #validate the input
    #create a booking
    booking = Booking(customer_name)
    return booking

def  get_customer_email():
    """ 
    Get the customer email, validate and add it to the booking
    """
    #customer input
    #validate
    #create booking
    booking = Booking(customer_email)

def select_therapy(booking):
    """ 
    Display types of therapy to the customer, validate and get therapy name
    """
    #display message
    #validate therapy 
    #get therapy name
    booking.set_therapy(therapy_name)
    return booking 
 
def select_therapist(booking):
    # display message
    # validate the selected therapist
    # get the therapist name
    booking.set_therapist(therapist)
    return booking   

def save_booking(booking):
    #make google sheet connection
    #make google sheet call and save the data

def main():
    booking = get_customer_name()
    booking = get_customer_email()
    select_therapy(booking)
    select_therapist(booking)
    save_booking(booking)

selection = 1

if not selection.isnumeric() or not (int(selection) < Therapies.length and int(selection) > 0)

def getSelectedTherapy(selection):
    return THERAPIES[selection-1]: