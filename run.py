# Settings and credentials to allow access to Google Sheets
import gspread
from google.oauth2.service_account import Credentials

# Libraries
import datetime

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

            else:
                raise ValueError(
                    f"Please try again."
                )

        except ValueError as e:
            print()
            print(f"Invalid input: {e}")


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

            else:
                raise ValueError(
                    f"Please select one of the options (1-6)."
                )

        except ValueError as e:
            print()
            print(f"Invalid input: {e}")


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

            else:
                raise ValueError(
                    f"Description cannot be empty."
                )

        except ValueError as e:
            print()
            print(f"Invalid input: {e}")


# valid date input to be updated: 
# currently, future dates are accepted
# currently no limit on past dates
def validate_expense_date():
    """
    Validates user's expense date input.
    While loop will repeatedly request data until it is valid.
    """
    print("Please enter date as DD-MM-YYYY.")

    while True:
        try:
            global date_input
            date_input = input("> ")
            datetime.datetime.strptime(date_input, "%d-%m-%Y")
            return True
            
        except ValueError:
            print()
            print("Invalid format. Please enter date as DD-MM-YYYY.")


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
                    f"Please type 'c' to confirm or 'r' to re-enter details."
                )

        except ValueError as e:
            print()
            print(f"Invalid input: {e}")
    

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


# View Expenses Menu

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
                print("Showing expenses in order")
                break
                
            elif user_input == "2":
                print()
                print("Showing expenses by category")
                break

            elif user_input == "3":
                print()
                print("Returning to main menu... \n")
                main_menu()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-3)."
                )

        except ValueError as e:
            print()
            print(f"Invalid input: {e}")


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
                print("Opening Expenses Menu...\n")
                add_expenses()
                break
                
            elif user_input == "2":
                print()
                view_expenses()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-2)."
                )

        except ValueError as e:
            print()
            print(f"Invalid input: {e}")

# Run the main function
main_menu()
