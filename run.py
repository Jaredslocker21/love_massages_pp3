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

def get_client_info():
    """
    Get clients input data and add it to the google sheet 
    """

    data_str = input('Enter your name here\n')
    data_email = input('Enter your email here\n')
    print(f"Your name is {data_str}")
    print(f"Your email is {data_email}")

get_client_info()