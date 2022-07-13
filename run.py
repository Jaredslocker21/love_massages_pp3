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
             'Rehabilitation Massage', 'Relaxation']
THERAPISTS = ['Jared', 'Tor', 'Victoria','Akshat']


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


class Booking:
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def set_therapy_name(self, therapy_name):
        self.therapy_name = therapy_name

    def set_therapist_name(self, therapist_name):
        self.therapist_name = therapist_name

    def get_booking_data(self):
        return [self.customer_name, self.therapy_name, self.therapist_name]


def select_customer_name_and_get_booking():
    """
    The name_input function takes input from the user and stores it
    in a variable that can be used further into the program
    """
    customer_name = take_customer_name_input()
    print (colored((f"\nYour booking reference is {customer_name}\n"), "blue"))
    booking = Booking(customer_name)
    return booking


def take_customer_name_input():
    """
    Funtion takes customers name input and does validations is longer
    than 10 or not long enough.
    """
    try:
        customer_name = input("Please enter your"
                                " name for a booking:\n").capitalize()
        if len(customer_name) > 20:
            raise ValueError('INVALID NAME. Too long')
        elif len(customer_name) == 0:
             raise ValueError('Name cannot be empty')
        return customer_name
    except ValueError as error_msg:
        print(error_msg)
        return take_customer_name_input()



def set_therapy_name(booking):
    """
    The select_name_therapy function takes input from the user and stores it
    in a variable to be called by booking
    """
    try:
        print("Please choose your Therapy:")
        for idx, therapy in enumerate(THERAPIES):
            print("{}) {}".format(idx + 1, therapy))
        choice_idx = int(input("Enter choice: "))
        if choice_idx > 0 and choice_idx <= len(THERAPIES):
            print('You have chosen ' + THERAPIES[choice_idx - 1])
            booking.set_therapy_name(THERAPIES[choice_idx - 1])
            return booking
        raise ValueError("Invalid choice")
    except ValueError as error_msg:
        print(error_msg)
        return set_therapy_name(booking)


def set_therapist_name(booking):
    """
    The select_name_therapy function takes input from the user and stores it
    in a variable to be called by booking
    """
    try:
        print("\n Your Therapist's are: \n")
        for idx, therapy in enumerate(THERAPISTS):
            print("{}) {}".format(idx + 1, therapy))
        choice_idx = int(input("Enter choice: \n"))
        if choice_idx > 0 and choice_idx <= len(THERAPISTS):
            print('You have chosen ' + THERAPISTS[choice_idx - 1])
            booking.set_therapist_name(THERAPISTS[choice_idx - 1])
            return booking
        raise ValueError("Invalid choice")
    except ValueError as error_msg:
        print(error_msg)
        return set_therapist_name(booking)


def update_worksheet(booking):
    """
    Receives list of intergers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
        """
    print(colored((f"Updating our bookings is in progress.\n"), "magenta"))
    worksheet_to_update = SHEET.worksheet("bookings")
    worksheet_to_update.append_row(booking.get_booking_data())
    print(colored(("Thank you {} for choosing {} for {}".format(booking.customer_name, booking.therapist_name, booking.therapy_name)), "yellow"))
    print(colored(("\nYour booking has been updated!\n"), "magenta"))
    print(colored(("Your therapist will be contacting you.\n"), "magenta"))



def main():
    welcome()
    booking = select_customer_name_and_get_booking()
    set_therapy_name(booking)
    set_therapist_name(booking)
    update_worksheet(booking)


main()