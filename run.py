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


def welcome():
    """
    Introduction to the Application.
    """
    print(colored(('Wellcome to Love Massages.\n'), 'cyan'))
    print(colored(('Enter your Name and your Email address when prompted below:'), 'cyan'))
    print(colored(('\n'), 'cyan'))
    print(colored(('Select your type of Massage Therapy \n'), 'cyan'))
    print(colored(('After that select your Massage Therapist.\n'), 'cyan'))
    print(colored(('All your selections will be logged with our administration and your therapist will contact you with more information.\n'), 'cyan'))
    
welcome()

client_info = []
# love sandwiches example
def get_client_info():
    """
    Get clients input data and add it to the google sheet 
    """
    data_str = input('Enter your name here\n')
    data_email = input('Enter your email here\n')
    print(f"Your name is {data_str}")
    print(f"Your email is {data_email}")

    

def verify_client_info():
    """
    verify name and email is entered correctly letters and email
    """
    while True:
        try:

def update_client_worksheet():
    """
    Update client information and append worksheet to a new row
    """


update_client_worksheet()
verify_client_info()
get_client_info()

def index_offered_therapy():
    """
    Function to index available  therapies
    """
    titles = therapy_titles():
    index = 1
    for title in titles:
        print(f' {index}. {title}')
        index += 1
# Retrieve the different types of therapies from google docs
def retrieve_therapy():
    """
  Display Therapies
    """
    print('\n Select the therapy you would like.')
    print(' Choose the therapy 1,2 or 3.\n')

    index_offered_therapy()

    selection = input('\n Please select a desired therapy numbers 1,2 or 3:\n ')

    if selection == '1':
        therapy_list('Occupational')
    elif selection == '2':
        therapy_list('Sports')
    elif selection == '3':
        therapy_list('Rehabilitation')
    else:
        print('\n Invalid choice.')
        print(' You may only choose one of the listed options.\n')
        return retrieve_therapy()

    print('\n Great Choice!')
   
def update_client_worksheet():
    """
    Update client information worksheet to append new column - type of therapy 
    """
# Choose your therapist, 
def retrieve_therapist():
    """
    Function to display a Therapist,
    and allow the user to select their therapist.
    """
    print('\n Select the therapist you would like.')
    print(' Choose the therapist 1,2 or 3.\n')

    index_therapist():

    selection = input('\n Please select a therapist numbers 1,2 or 3:\n ')

    if selection == '1':
        therapy_list('Jared')
    elif selection == '2':
        therapy_list('Tor')
    elif selection == '3':
        therapy_list('Victoria')
    else:
        print('\n Invalid choice.')
        print(' You may only choose one of the listed options.\n')
        return retrieve_therapist()

    print('\n Great Choice!')
   

def index_therapist():
    """
    Function to index available  therapies
    """
    titles = therapist_name()
    index = 1
    for title in titles:
        print(f' {index}. {title}')
        index += 1






def main()
    """
    run all functions
    """
