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
    """
    #print("Expense Amount:")

    while True:
        print("Expense Amount:")

        try:
            user_choice = float(input("> "))
            if user_choice != "":
                print("Well done")
                break

            else:
                raise ValueError(
                    f"Please try again."
                )

        except ValueError as e:
            print()
            print(f"Invalid Input: {e}\n")


def validate_expense_category():
    """
    Validate user's expense category input.
    """
    print("Please enter a category (1-6):")

    while True:
        print()
        print("1. Housing")
        print("2. Food")
        print("3. Transportation")
        print("4. Entertainment")
        print("5. Healthcare")
        print("6. Misc")
        print()

        try:
            user_choice = input("> ")
            if user_choice in ["1", "2", "3", "4", "5", "6"]:
                print()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-6)."
                )

        except ValueError as e:
            print()
            print(f"Invalid Input: {e}")


def validate_expense_description():
    """
    Validates user's expense description input.
    """
    print("Please enter a description.")

    while True:
        #expense_description = input("Expense Description: ")

        try:
            user_choice = input("> ")
            #if expense_description != "":
            if user_choice != "":
                break

            else:
                raise ValueError(
                    f"Description cannot be empty."
                )

        except ValueError as e:
            print()
            print(f"Invalid Input: {e}\n")


# valid date input to be updated: 
# currently, future dates are accepted
# currently no limit on past dates 
def validate_expense_date(date_input):
    """
    Validates user's expense date input.
    """
    while True:
        
        try:
            datetime.datetime.strptime(date_input, "%d-%m-%Y")
            return True
            
        except ValueError:
            print("Invalid format. Please enter date as DD-MM-YYYY.\n")
            date_input = input("Expense Date (DD-MM-YYYY): ")
            

def add_expenses():
    """
    Collects expense details from the user.
    """
    print()
    print("*** Add Expenses Menu *** \n")
    print("Please add expense details below:")
    print()
    expense_date = input("Expense Date (DD-MM-YYYY): ")
    print()
    validate_expense_date(expense_date)
    print()
    validate_expense_description()
    print()
    validate_expense_category()
    print()
    validate_expense_amount()


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
            user_choice = input("> ")
            if user_choice == "1":
                print()
                print("Showing expenses in order")
                break
                
            elif user_choice == "2":
                print()
                print("Showing expenses by category")
                break

            elif user_choice == "3":
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
            print(f"Invalid Input: {e}\n")


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
            user_choice = input("> ")
            if user_choice == "1":
                print()
                print("Opening Add Expenses Menu...\n")
                add_expenses()
                break
                
            elif user_choice == "2":
                print()
                view_expenses()
                break

            else:
                raise ValueError(
                    f"Please select one of the options (1-2)."
                )

        except ValueError as e:
            print()
            print(f"Invalid Input: {e}\n")


main_menu()
#validate_expense_amount()