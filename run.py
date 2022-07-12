"""
Import section
"""
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

THERAPIES = ['Occupational Massage:', 'Sports Massage:',
             'Rehabilitation Massage:']
THERAPISTS = ['Jared:', 'Tor:', 'Victoria:']


def welcome():
    """
    Introduction to the Application.
    """
    print(colored(('As a current member of Love Massages.\n'), 'cyan'))
    print(colored(('You are welcome to a FREE Massage.\n'), 'cyan'))
    print(colored(('Enter your Name when prompted below:\n'), 'cyan'))
    print(colored(('Select your type of Massage Therapy \n'), 'cyan'))
    print(colored(('Select your Therapist.\n'), 'cyan'))
    print(colored(('Your booking will be made.\n'), 'cyan'))
    print(colored(('We will contact you shortly\n'), 'cyan'))
    


welcome()


class Booking:
    def __init__(self, customer_name,):
        self.customer_name = customer_name

    def select_therapy_name(self, select_therapy_name):
        self.therapy_name = select_therapy_name

    def select_therapist_name(self, select_therapist_name):
        self.therapist_name = select_therapist_name

    def get_booking_data(self):
        return [self.customer_name, self.therapy_name, self.therapist_name]


def select_customer_name():
    """
    The name_input function takes input from the user and stores it
    in a variable that can be used further into the program
    """
    while True:
        customer_name = input("Please enter your"
                              " name for a booking:\n").capitalize()
        if check_customer_name(customer_name):
            break
    print (colored((f"\nYour booking reference is {customer_name}\n"), "blue"))
    booking = Booking(customer_name)
    return booking


def check_customer_name(name):
    """
    Funtion checks if the customers name is longer
    than 10 or not long enough.
    """
    if len(name) > 20:
        print('INVALID NAME. Too long')
        return False
    elif len(name) == 0:
        print('Please enter your name')
    else:
        return True


def select_therapy_name(booking):
    """
    The select_name_therapy function takes input from the user and stores it
    in a variable to be called by booking
    """
    while True:
        print("\n Please select the type of Therapy.\n")
        print(*THERAPIES, sep='\n')
        therapy_name = input("Please enter therapy:\n").capitalize()
        if check_therapy_name(therapy_name):
            break
    print(colored((f"\n You have chosen {therapy_name}\n"), "blue"))
    booking.select_therapy_name(therapy_name)
    return booking


def check_therapy_name(name):
    """
    Check if ther Therapy Chosen is Correct
    """
    if len(name) > 20:
        print('INVALID NAME. Too long')
        return False
    elif len(name) == 0:
        print('Please enter your therapy name')
    else:
        return True


def select_therapist_name(booking):
    """
    The select_name_therapist function takes
    input from the user and stores it
    as a variable( to be called later to print booking
    """
    while True:
        print("\n Your Therapist's are: \n")
        print(*THERAPISTS, sep='\n')
        therapist_name = input("Please type Therapist name:\n").capitalize()
        if check_therapist_name(therapist_name):
            break
    print(colored((f"\n You have chosen {therapist_name}\n"), "blue"))
    booking.select_therapist_name(therapist_name)
    return booking


def check_therapist_name(name):
    """
    Check if the Therapist Chosen is Correctly
    """
    if len(name) > 20:
        print('INVALID THERAPIST')
        return False
    elif len(name) <= 0:
        print('Please enter the therapist name')
    else:
        return True


def update_worksheet(data, worksheet):
    """
    Receives list of intergers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
        """
    print(colored((f"Updating our {worksheet} is in progress.\n"), "magenta"))
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data.get_booking_data())
    print(colored(("Thank you for choosing Love Massages!\n"), "magenta"))
    print(colored(("Your booking has been updated!\n"), "magenta"))
    print(colored(("Your therapist will be contacting you.\n"), "magenta"))


def main():
    booking = select_customer_name()
    select_therapy_name(booking)
    select_therapist_name(booking)
    update_worksheet(booking, "bookings")


main()