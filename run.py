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
# love sandwiches example

def get_client_info():
    """
    Get clients input data and add it to the google sheet 
    """
    data_str = input('Enter your name here\n')
    data_email = input('Enter your email here\n')
    print(f"Your name is {data_str}")
    print(f"Your email is {data_email}")

# #def validate_data(values):

#     print()

get_client_info()

# def therapy_list():
#     """
#     retun a list of therapies and definitions for the client to choose
#     """
#     print('Select "1" for Occupational Therapy')
#     print('Select "2" for Sports Therapy')
#     print('Select "3" for Rehabilitation Therapy')


# therapy_list()  



# def main():
#     """
#     Run all program functions
#     """
#     data = get_client_data()
#     client_data = [int(num) for num in data]
#     update_worksheet(client_data, "client")
#     new_client_data = match_client_data(client_data)
#     receipt_for_client = new_client_data   
#     update_worksheet(stock_data, "stock")



# main()