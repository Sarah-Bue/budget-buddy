# Settings and credentials to allow access to Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# Libraries
import datetime
from pprint import pprint

# Import and initialize colorama for text formatting
# Tutorial found here: https://linuxhint.com/colorama-python/
import colorama
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


# Add Expenses Menu

def validate_expense_amount():
    """
    Validates user's expense amount input.
    While loop will repeatedly request data until it is valid.
    """

    while True:
        print("Please enter an amount:")

        try:
            global amount_input
            amount_input = float(input("> "))
            if amount_input != "":
                break

            elif amount_input == "exit":
                main_menu()

            else:
                raise ValueError(
                    f"Please try again."
                )

        except ValueError as e:
            print()
            print(Fore.RED + f"Invalid input: {e}")


def validate_expense_category():
    """
    Validate user's expense category input.
    While loop will repeatedly request data until it is valid.
    """
    print("Please select a category (1-6).")

    while True:
        print("     1. Housing")
        print("     2. Food")
        print("     3. Transportation")
        print("     4. Entertainment")
        print("     5. Healthcare")
        print("     6. Misc")
        print()

        try:
            global category_input
            category_input = input("> ")
            if category_input in ["1", "2", "3", "4", "5", "6"]:
                break

            elif category_input == "exit":
                main_menu()

            else:
                raise ValueError(
                    f"Please select one of the options (1-6)."
                )

        except ValueError as e:
            print()
            print(Fore.RED + f"Invalid input: {e}")


def validate_expense_description():
    """
    Validates user's expense description input.
    While loop will repeatedly request data until it is valid.
    """
    print("Please enter a description.")

    while True:
        try:
            global description_input
            description_input = input("> ")
            if description_input != "":
                break

            elif description_input == "exit":
                main_menu()

            else:
                raise ValueError(
                    f"Description cannot be empty."
                )

        except ValueError as e:
            print()
            print(Fore.RED + f"Invalid input: {e}")


def validate_expense_date():
    """
    Validates user's expense date input.
    While loop will repeatedly request data until it is valid.
    This function accepts dates from 01.01.2024 to the current date.
    """
    print("Please enter date as DD-MM-YYYY.")

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
                main_menu()

            else:
                print()
                print(Fore.RED + "Please enter a date between 01-01-2024 and today.")

        except ValueError:
            print()
            print(Fore.RED + "Invalid format. Please enter date as DD-MM-YYYY.")


def confirm_input():
    """
    Allows user to confirm or update expense details.
    While loop will repeatedly request data until it is valid.
    """
    print(f"You have entered:")
    print(f"     Expense Date: {date_input}")
    print(f"     Expense Description: {description_input}")
    print(f"     Expense Category: {category_input}")
    print(f"     Expense Amount: {amount_input}")
    print()
    print("Conrifm expense details (c) or re-enter (r)?")

    while True:
        try:
            user_input = input("> ")
            if user_input == "r" or user_input == "R":
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
            print(Fore.RED + f"Invalid input: {e}")
    

def add_expenses():
    """
    Collects expense details from the user.
    After all data is collected and validated, a summary is shown to the user.
    """
    print("*** Add Expenses Menu *** \n")
    print("Please add expense details below.")
    print("To return to Main Menu, please enter 'exit'.")
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
    print("Updating sales worksheet...\n")
    expenses_worksheet = SHEET.worksheet("expenses")
    expenses_worksheet.append_row(expense)
    print("Worksheet updated successfully.\n")
    print("Add another expense (a) or return to main menu (m) ?")

    while True:
        try:
            user_input = input("> ")
            if user_input == "a" or user_input == "A":
                add_expenses()

            elif user_input == "m" or user_input =="M":
                print("Loading Main Menu...")
                main_menu()
                break

            else:
                raise ValueError(
                    f"Please enter 'a' to add another expense or 'm' to return to the main menu."
                )

        except ValueError as e:
            print()
            print(Fore.RED + f"Invalid input: {e}")


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



def view_expenses():
    """
    Runs the expense view menu.
    Allows the user to select how they want to view their expenses.
    """
    while True:
        print()
        print("*** View Expenses Menu *** \n")
        print("Please select one of the options:")
        print("1. View in Order")
        print("2. View by Category")
        print("3. Return to Main Menu")
        print()

        try:
            user_input = input("> ")
            if user_input == "1":
                print()
                print("Loading Expenses...\n")
                view_in_order(expenses)
                break
                
            elif user_input == "2":
                print()
                print("Loading Expenses...\n")
                view_by_category(expenses)
                break

            elif user_input == "3":
                print()
                print("Loading Main Menu...\n")
                main_menu()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-3)."
                )

        except ValueError as e:
            print()
            print(Fore.RED + f"Invalid input: {e}")


# Main Menu

def main_menu():
    """
    Runs the main menu of the program.
    Allows the user to navigate to one of two sub-menus.
    """
    while True:
        print()
        print("*** Main Menu *** \n")
        print("Please select one of the options:")
        print("1. Add Expenses")
        print("2. View Expenses")
        print()

        try:
            user_input = input("> ")
            if user_input == "1":
                print()
                print("Loading Expenses Menu...\n")
                add_expenses()
                break
                
            elif user_input == "2":
                print("Loading View Menu...\n")
                view_expenses()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-2)."
                )

        except ValueError as e:
            print()
            print(Fore.RED + f"Invalid input: {e}")

# Run the main function
main_menu()
