# Libraries
import gspread
from google.oauth2.service_account import Credentials
import datetime
from pprint import pprint
import os
import colorama
import time
import sys


# Initialize colorama for text formatting
# Tutorial found here: https://linuxhint.com/colorama-python/
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# Scope for Google IAM for API access
# Guidance provided by Code Institute's course material
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Variables to access spreadsheet
# Guidance provided by Code Institute's course material
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('expense_tracker')
expenses = SHEET.worksheet("expenses")
data = expenses.get_all_values()

# General

# Tutorial and code found here: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
    """
    Function for clearing CLI for new code.
    """
    os.system("clear")


# Tutorial and code found here: https://www.101computing.net/python-typing-text-effect/
def typingPrint(text):
    """
    Replaces print() with typingPrint() to create typing effect.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
  
# Tutorial and code found here: https://www.101computing.net/python-typing-text-effect/
def typingInput(text):
    """
    Replaces input() with typingInput() to create typing effect.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value


def program_start():
    """
    Displays logo to welcome the user.
    """
    print()
    print(Fore.GREEN + Style.BRIGHT + '''
    **********************************************************************
                                                                        
    888888ba                 dP                     dP   
    88    `8b                88                     88   
   a88aaaa8P' dP    dP .d888b88 .d8888b. .d8888b. d8888P 
    88   `8b. 88    88 88'  `88 88'  `88 88ooood8   88   
    88    .88 88.  .88 88.  .88 88.  .88 88.  ...   88   
    88888888P `88888P' `88888P8 `8888P88 `88888P'   dP   
                                    .88                 
                                d8888P

    888888ba                 dP       dP                 
    88    `8b                88       88                 
   a88aaaa8P' dP    dP .d888b88 .d888b88 dP    dP        
    88   `8b. 88    88 88'  `88 88'  `88 88    88        
    88    .88 88.  .88 88.  .88 88.  .88 88.  .88        
    88888888P `88888P' `88888P8 `88888P8 `8888P88        
                                            .88        
                                        d8888P         
                                                                        
    **********************************************************************
    ''')
    time.sleep(3)
    clearScreen()


# Add Expenses Menu

def validate_expense_amount():
    """
    Validates user's expense amount input.
    While loop will repeatedly request data until it is valid.
    """

    while True:
        typingPrint("Please enter an amount:\n")

        try:
            global amount_input
            amount_input = float(input("> "))
            if amount_input != "":
                break

            elif amount_input == "exit":
                time.sleep(1.5)
                clearScreen()
                main_menu()

            else:
                raise ValueError(
                    f"Please try again."
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")


def validate_expense_category():
    """
    Validate user's expense category input.
    While loop will repeatedly request data until it is valid.
    """
    typingPrint("Please select a category (1-6).\n")

    while True:
        print("    1. Housing")
        print("    2. Food")
        print("    3. Transportation")
        print("    4. Entertainment")
        print("    5. Healthcare")
        print("    6. Misc")
        print()

        try:
            global category_input
            category_input = input("> ")
            if category_input in ["1", "2", "3", "4", "5", "6"]:
                break

            elif category_input == "exit":
                time.sleep(1.5)
                clearScreen()
                main_menu()

            else:
                raise ValueError(
                    f"Please select one of the options (1-6)."
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")


def validate_expense_description():
    """
    Validates user's expense description input.
    While loop will repeatedly request data until it is valid.
    """
    typingPrint("Please enter a description.\n")

    while True:
        try:
            global description_input
            description_input = input("> ")
            if description_input != "":
                break

            elif description_input == "exit":
                time.sleep(1.5)
                clearScreen()
                main_menu()

            else:
                raise ValueError(
                    f"Description cannot be empty."
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")


def validate_expense_date():
    """
    Validates user's expense date input.
    While loop will repeatedly request data until it is valid.
    This function accepts dates from 01.01.2024 to the current date.
    """
    typingPrint("Please enter date as DD-MM-YYYY.\n")

    while True:
        try:
            global date_input
            date_input = input("> ")
            new_date = datetime.datetime.strptime(date_input, "%d-%m-%Y")

            min_date = datetime.datetime(2024, 1, 1)
            max_date = datetime.datetime.now()

            if min_date <= new_date and new_date <= max_date:
                return new_date

            elif date_input == "exit":
                time.sleep(1.5)
                clearScreen()
                main_menu()

            else:
                print()
                print(Fore.RED + "Please enter a date between 01-01-2024 and today.")

        except ValueError:
            print()
            typingPrint(Fore.RED + "Invalid format. Please enter date as DD-MM-YYYY.")


def confirm_input():
    """
    Allows user to confirm or update expense details.
    While loop will repeatedly request data until it is valid.
    """
    time.sleep(1.5)
    clearScreen()

    print(f"You have entered:")
    print(f"     Expense Date: {date_input}")
    print(f"     Expense Description: {description_input}")
    print(f"     Expense Category: {category_input}")
    print(f"     Expense Amount: {amount_input}")
    print()
    typingPrint("Conrifm expense details (c) or re-enter (r)?\n")

    while True:
        try:
            user_input = input("> ")
            if user_input == "r" or user_input == "R":
                time.sleep(1.5)
                clearScreen()
                add_expenses()

            elif user_input == "c" or user_input =="C":
                entered_expense = [date_input, description_input, category_input, amount_input]

                print()
                update_worksheet(entered_expense)
                print()
                break

            else:
                raise ValueError(
                    f"Please enter 'c' to confirm or 'r' to re-enter details."
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")
    

def add_expenses():
    """
    Collects expense details from the user.
    After all data is collected and validated, a summary is shown to the user.
    """
    print("*** Add Expenses Menu *** \n")
    typingPrint("Please add expense details below.\n")
    typingPrint("To return to Main Menu, please enter 'exit'.\n")
    print()
    validate_expense_date()
    print()
    validate_expense_description()
    print()
    validate_expense_category()
    print()
    validate_expense_amount()
    print()
    confirm_input()

def update_worksheet(expense):
    """
    Updates the worksheet.
    Appends a new row with the provided expense details.
    """
    typingPrint("Updating sales worksheet...\n")
    expenses_worksheet = SHEET.worksheet("expenses")
    expenses_worksheet.append_row(expense)
    typingPrint("Worksheet updated successfully.\n")
    typingPrint("Add another expense (a) or return to main menu (m)?\n")

    while True:
        try:
            user_input = input("> ")
            if user_input == "a" or user_input == "A":
                time.sleep(1.5)
                clearScreen()
                add_expenses()

            elif user_input == "m" or user_input =="M":
                typingPrint("Loading Main Menu...\n")
                time.sleep(1.5)
                clearScreen()
                main_menu()
                break

            else:
                raise ValueError(
                    f"Please enter 'a' to add another expense or 'm' to return to the main menu."
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")


# View Expenses Menu

#def sort_by_category():
#    """
#    Sorts expenses by category, from highest to lowest spent category.
#    """

#def calculate_category_totals():
#    """
#    Calculates total expenses for each category.
#    """

#def view_by_category(expenses):
#    print("Displaying expenses by category...")
#    """
#    Displays expenses by category, from highest to lowest spent category.
#    """


#def sort_by_date(data):
#    """
#    Sorts expense inputs by date, from oldest to newest.
#    """

#currently shows expenses in the order they were entered rather than by date
def view_in_order(expenses):
    """
    Displays expenses in the order they were entered.
    """
    expenses_total = SHEET.worksheet("expenses").get_all_values()
    pprint(expenses_total)
    print()
    typingPrint("To return to the main menu, please enter 'm'.\n")

    while True:

        try:
            user_input = input("> ")
            if user_input == "m" or user_input == "M":
                print()
                typingPrint("Loading Main Menu...\n")
                time.sleep(1.5)
                clearScreen()
                main_menu()
                break

            else:
                raise ValueError(
                    f"Please enter 'm' to return to the main menu.\n"
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")


def view_expenses():
    """
    Runs the expense view menu.
    Allows the user to select how they want to view their expenses.
    """
    while True:
        print()
        print("*** View Expenses Menu *** \n")
        typingPrint("Please select one of the options:\n")
        print()
        print("    1. View in Order")
        print("    2. View by Category")
        print("    3. Return to Main Menu")
        print()

        try:
            user_input = input("> ")
            if user_input == "1":
                print()
                typingPrint("Loading Expenses...\n")
                time.sleep(1.5)
                clearScreen()
                view_in_order(expenses)
                break
                
            elif user_input == "2":
                print()
                typingPrint("Loading Expenses...\n")
                time.sleep(1.5)
                clearScreen()
                view_by_category(expenses)
                break

            elif user_input == "3":
                print()
                typingPrint("Loading Main Menu...\n")
                time.sleep(1.5)
                clearScreen()
                main_menu()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-3)."
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")


# Main Menu

def main_menu():
    """
    Runs the main menu of the program.
    Allows the user to navigate to one of two sub-menus.
    """
    while True:
        print()
        print("*** Main Menu *** \n")
        typingPrint("Please select one of the options:\n")
        print()
        print("    1. Add Expenses")
        print("    2. View Expenses")
        print()

        try:
            user_input = input("> ")
            if user_input == "1":
                print()
                typingPrint("Loading Expenses Menu...\n")
                time.sleep(1.5)
                clearScreen()
                add_expenses()
                break
                
            elif user_input == "2":
                print()
                typingPrint("Loading View Menu...\n")
                time.sleep(1.5)
                clearScreen()
                view_expenses()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-2)."
                )

        except ValueError as e:
            print()
            typingPrint(Fore.RED + f"Invalid input: {e}")


# Run the main function
program_start()
main_menu()

