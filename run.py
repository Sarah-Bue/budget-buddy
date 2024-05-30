# Libraries
import datetime
import os
import sys
import time

import colorama
import gspread

from collections import defaultdict
from colorama import Back, Fore, Style
from google.oauth2.service_account import Credentials
from tabulate import tabulate

# Initialize colorama for text formatting
# Tutorial: https://linuxhint.com/colorama-python/
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
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("expense_tracker")
expenses = SHEET.worksheet("expenses")
data = expenses.get_all_values()


# General Functions

# Code adapted from: https://www.101computing.net/python-typing-text-effect/
def clearScreen():
    """
    Function for clearing CLI for new code.
    """
    os.system("clear")


# Code adapted from: https://www.101computing.net/python-typing-text-effect/
def typingPrint(text, color=Fore.WHITE):
    """
    Replaces print() with typingPrint() to create typing effect.
    """
    for character in text:
        sys.stdout.write(color + character)
        sys.stdout.flush()
        time.sleep(0.05)


def pause_and_clear():
    """
    Clears screen after a brief pause.
    """
    time.sleep(1.5)
    clearScreen()


# ASCII art generator: https://manytools.org/hacker-tools/ascii-banner/
def welcome_screen():
    """
    Displays logo and intro text.
    """
    # Logo
    print(Fore.CYAN + r'''
            ══════════════════════════════════════════════════════
     _               _                     _               _     _
    | |             | |            _      | |             | |   | |
    | | _  _   _  _ | | ____  ____| |_    | | _  _   _  _ | | _ | |_   _
    | || \| | | |/ || |/ _  |/ _  )  _)   | || \| | | |/ || |/ || | | | |
    | |_) ) |_| ( (_| ( ( | ( (/ /| |__   | |_) ) |_| ( (_| ( (_| | |_| |
    |____/ \____|\____|\_|| |\____)\___)  |____/ \____|\____|\____|\__  |
                      (_____|                                     (____/

            ══════════════════════════════════════════════════════
    ''')

    # Intro to explain program purpose
    print("Welcome to Budget Buddy, the friend you didn't know you needed.\n")
    print("The first step towards financial success is self-awareness.")
    print("Budget Buddy allows you to easily add "
          "and review your expenses on the go.\n")
    typingPrint("                       Loading, please wait...", Fore.YELLOW)
    time.sleep(4)
    clearScreen()


# Add Expenses Menu Functions

def validate_expense_amount():
    """
    Validates user's expense amount input.
    While loop will repeatedly request data until it is valid.
    """
    typingPrint("Please enter an amount:\n")

    # Loop repeats until valid inuput is received
    while True:
        # Try... except for exception / error handling
        try:
            # global so variable can be accessed in other functions
            global amount_input
            amount_input = float(input("> "))

            # Input cannot be empty
            # Input must be between 0 and 10000
            if amount_input != "" and 0 <= amount_input <= 10000:
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: Please enter a number "
                        "between 0 and 10000.\n", Fore.RED)


def validate_expense_category():
    """
    Validate user's expense category input.
    While loop will repeatedly request data until it is valid.
    """
    # global so variable can be accessed in other functions
    global expense_categories
    expense_categories = [
        "Housing", "Food", "Transportation", "Entertainment", "Healthcare",
        "Misc"
    ]

    typingPrint("Please select a category (1-6).\n")

    # Loop repeats until valid inuput is received
    while True:
        # Loop through each list item & print with corresponding index number
        # +1 to display index as 1-6 rather than 0-5
        for i, expense_category in enumerate(expense_categories):
            print(f"    {i+1}. {expense_category}")

        # Try... except for exception / error handling
        try:
            # -1 to get "true" index number rather than displayed index number
            user_input = int(input("> ")) - 1

            # Only integers 1-6 valid
            if user_input in range(6):
                # global so variable can be accessed in other functions
                global category_input
                category_input = expense_categories[user_input]
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint(
                "Invalid input: "
                "Please enter one of the options (1-6).\n", Fore.RED)


def validate_expense_description():
    """
    Validates user's expense description input.
    While loop will repeatedly request data until it is valid.
    """
    typingPrint("Please enter a description.\n")

    # Loop repeats until valid inuput is received
    while True:
        # Try... except for exception / error handling
        try:
            # global so variable can be accessed in other functions
            global description_input
            description_input = input("> ")

            # Input cannot be empty
            # Input cannot be longer than 25 characters
            if description_input != "" and len(description_input) < 50:
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: "
                        "Please enter a description between "
                        "0 and 50 characters.\n", Fore.RED)


def validate_expense_date():
    """
    Validates user's expense date input.
    While loop will repeatedly request data until it is valid.
    This function accepts dates from 01.01.2024 to the current date.
    """
    typingPrint("Please enter date as DD-MM-YYYY.\n")

    # Loop repeats until valid inuput is received
    while True:
        # Try... except for exception / error handling
        try:
            global date_input
            date_input = input("> ")

            # Turns date_input into datetime object
            # %d-%m-%Y = DD-MM-YYYY
            new_date = datetime.datetime.strptime(date_input, "%d-%m-%Y")

            # Set date range to 01-01-2024 - today(dynamic)
            min_date = datetime.datetime(2024, 1, 1)
            max_date = datetime.datetime.now()

            # Check that date_input is in valid date range
            if min_date <= new_date and new_date <= max_date:
                return new_date

            # Invalid input raises error
            else:
                print()
                typingPrint(
                    "Invalid input: "
                    "Date must be between 01-01-2024 and today."
                    "\n", Fore.RED)

        except ValueError:
            print()
            typingPrint("Invalid input: "
                        "Please enter date as DD-MM-YYYY.\n", Fore.RED)


def confirm_input():
    """
    Allows user to confirm or update expense details.
    While loop will repeatedly request data until it is valid.
    """
    typingPrint("                       Summarizing expenses...\n",
                Fore.YELLOW)
    pause_and_clear()

    print()
    print(Fore.CYAN + "                  ◇─◇──◇── ADD EXPENSES ──◇──◇─◇\n")

    print("         ══════════════════════════════════════════════════════")
    print()
    print("Your expense details:")
    print()
    print(f"     Expense Date: {date_input}")
    print(f"     Expense Description: {description_input.title()}")
    print(f"     Expense Category: {category_input}")
    print(f"     Expense Amount: € {amount_input}")
    print()
    print("         ══════════════════════════════════════════════════════")
    print()
    typingPrint("Conrifm expense details (c) or re-enter (r)?\n")

    # Loop repeats until valid inuput is received
    while True:
        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Re-enter details
            if user_input.lower() == "r":
                typingPrint("                       Clearing expense data..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                add_expenses()

            # Confirm details
            elif user_input.lower() == "c":
                entered_expense = [
                    date_input,
                    description_input,
                    category_input,
                    amount_input
                ]

                print()
                update_worksheet(entered_expense)
                print()
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint(
                "Invalid input: Please enter (c) to confirm "
                "or (r) to re-enter details.\n", Fore.RED)


def add_expenses():
    """
    Collects expense details from the user.
    Runs separate function to collect each aspect of details in order.
    After all data is collected and validated, a summary is shown to the user.
    """
    print()
    print(Fore.CYAN + "                  ◇─◇──◇── ADD EXPENSES ──◇──◇─◇\n")
    typingPrint("Please add expense details below.\n")
    print()
    print("         ══════════════════════════════════════════════════════")
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
    typingPrint("                       Updating worksheet...\n", Fore.YELLOW)
    print()
    # Adds added expense to google sheet as a new row
    expenses_worksheet = SHEET.worksheet("expenses")
    expenses_worksheet.append_row(expense)
    typingPrint("                  Worksheet updated successfully."
                "\n", Fore.GREEN)
    print()
    typingPrint("Add another expense (a) or return to Main Menu (m)?\n")
    print()

    # Loop repeats until valid inuput is received
    while True:
        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Add another expense
            if user_input.lower() == "a":
                pause_and_clear()
                add_expenses()

            # Return to main menu
            elif user_input.lower() == "m":
                print()
                return_to_main()
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint(
                "Invalid input: "
                "Please enter (a) to add another expense "
                "or (m) to return to Main Menu.\n", Fore.RED)


# View Expenses Menu Functions


def calculate_total_expenses(data):
    """
    Calculates the sum of all expenses.
    """
    # total_expenses starts out empty / at 0
    total_expenses = 0

    # Loops through each entry
    # Adds floats in 3rd index (= 4th column) together
    for entry in data:
        total_expenses += float(entry[3])
    return total_expenses


def view_by_category(data):
    """
    Calculates total expenses for each category.
    Displays categories in descending order.
    """
    # Create empty dictionary to store totals per category
    category_totals = {}

    # Loops through data
    # Categories at index 2 (= column 3), amounts at index 3 (= column 4)
    for entry in data:
        category = entry[2]
        amount = float(entry[3])

        # Update category totals if category is listed
        # Create new category if category is not listed
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    # Sort category totals in descending order
    # Adapted from: https://realpython.com/sort-python-dictionary/
    sorted_category_totals = dict(
        sorted(category_totals.items(), key=lambda item: item[1],
               reverse=True))

    # Calls calculate_total_expenses function
    total_expenses = calculate_total_expenses(data)

    print()
    print(Fore.CYAN + "                  ◇─◇──◇── VIEW EXPENSES ──◇──◇─◇\n")
    print("Viewing Expenses by Category")
    print()
    print("         ══════════════════════════════════════════════════════")
    print()
    # Table view of expenses by category
    print(tabulate(sorted_category_totals.items(),
                   headers=[
                        "Category",
                        "Total Expenses"
                    ]))
    print()
    print(f"                          Total Expenses: € {total_expenses}")
    print("         ══════════════════════════════════════════════════════\n")
    print()

    typingPrint("To return to Main Menu, please enter (m).\n")
    typingPrint("To switch to Date View, please enter (d).\n")
    typingPrint("To switch to Month View, please enter (v).\n")

    # Loop repeats until valid inuput is received
    while True:
        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Return to main menu
            if user_input.lower() == "m":
                print()
                return_to_main()
                break

            # Switch to date view
            # Uppercase and lowercase entry accepted
            elif user_input.lower() == "d":
                print()
                typingPrint("                       Loading Date View..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_date()
                break

            # Switch to month view
            # Uppercase and lowercase entry accepted
            elif user_input.lower() == "v":
                print()
                typingPrint("                       Loading Month View..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_month(data)
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint(
                "Invalid input: Please enter (m) "
                "to return to Main Menu "
                "or (d) to switch to Date View "
                "or (v) to switch to Month View.\n", Fore.RED)


def view_by_date():
    """
    Displays expenses sorted by date.
    Allows user to return to main menu after viewing expenses.
    """
    # Call calculate_total_expenses function
    total_expenses = calculate_total_expenses(data)

    # Table view of expenses
    print()
    print(Fore.CYAN + "                  ◇─◇──◇── VIEW EXPENSES ──◇──◇─◇\n")
    print("Viewing Expenses by Date")

    # Adapted from: https://docs.python.org/3/library/datetime.html
    # Adapted from: https://docs.python.org/3/howto/sorting.html
    # Each element (x) in the list gets turned into datetime object
    sorted_data = sorted(
        data, key=lambda x: datetime.datetime.strptime(x[0], "%d-%m-%Y"))

    print()
    print("         ══════════════════════════════════════════════════════")
    print()
    # Table view of expenses by date
    print(tabulate(sorted_data,
                   headers=[
                        "Date",
                        "Description",
                        "Category",
                        "Amount"
                    ]))
    print()
    print(f"                          Total Expenses: € {total_expenses}")
    print("         ══════════════════════════════════════════════════════\n")
    print()

    typingPrint("To return to Main Menu, please enter (m).\n")
    typingPrint("To switch to Category View, please enter (c).\n")
    typingPrint("To switch to Month View, please enter (v).\n")

    # Loop repeats until valid inuput is received
    while True:
        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Return to main menu
            # Uppercase and lowercase entry accepted
            if user_input.lower() == "m":
                print()
                return_to_main()
                break

            # Switch to category view
            # Uppercase and lowercase entry accepted
            elif user_input.lower() == "c":
                print()
                typingPrint("                       Loading Category View..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_category(expenses.get_all_values())
                break

            # Switch to month view
            # Uppercase and lowercase entry accepted
            elif user_input.lower() == "v":
                print()
                typingPrint("                       Loading Month View..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_month(data)
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint(
                "Invalid input: Please enter (m) "
                "to return to Main Menu "
                "or (c) to switch to Category View "
                "or (v) to switch to Month View.\n", Fore.RED)


def view_by_month(data):
    """
    Breaks down expenses by month.
    Displays months, categories, and total expenses.
    """
    # Call calculate_total_expenses function
    total_expenses = calculate_total_expenses(data)

    # Adapted from: https://docs.python.org/3/tutorial/datastructures.html
    # Create dictionary to hold monthly expenses
    # All expenses start at 0
    monthly_expenses = defaultdict(
        lambda: {
            "Housing": 0,
            "Food": 0,
            "Transportation": 0,
            "Entertainment": 0,
            "Healthcare": 0,
            "Misc": 0,
            "Total": 0
        })

    # Loop through each entry and assign variables to columns
    for entry in data:
        # Date in 1st column, category in 3rd, amount in 4th column
        date_str = entry[0]
        category = entry[2]
        amount = float(entry[3])

        # Converts date string to datetime object
        # Adapted from: https://docs.python.org/3/library/datetime.html
        date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")
        # Extracts month and year from datetime object
        month_year = date_obj.strftime("%m / %Y")

        # Adds expenses to dictionary
        # Adds expenses to total expenses
        monthly_expenses[month_year][category] += amount
        monthly_expenses[month_year]["Total"] += amount

    # Declare headers and empty table for tabulate
    headers = [
        "Month", "House", "Food", "Transp", "Entert", "Health", "Misc", "Total"
    ]
    table = []

    # Loop through each month and add to table
    for month, expenses in sorted(monthly_expenses.items()):
        # Create a list for each month
        row = [month] + list(expenses.values())
        # Add row to the table
        table.append(row)

    print()
    print(Fore.CYAN + "                  ◇─◇──◇── VIEW EXPENSES ──◇──◇─◇\n")
    print("Viewing Expenses by Month")
    print()
    print("         ══════════════════════════════════════════════════════")
    print()
    # Table view of expenses by month
    print(tabulate(table, headers=headers))
    print()
    print(f"                          Total Expenses: € {total_expenses}")
    print("         ══════════════════════════════════════════════════════")
    print()
    typingPrint("To return to Main Menu, please enter (m).\n")
    typingPrint("To switch to Date View, please enter (d).\n")
    typingPrint("To switch to Category View, please enter (c).\n")

    # Loop repeats until valid inuput is received
    while True:

        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Return to main menu
            # Uppercase and lowercase entry accepted
            if user_input.lower() == "m":
                print()
                return_to_main()
                break

            # Switch to date view
            # Uppercase and lowercase entry accepted
            elif user_input.lower() == "d":
                print()
                typingPrint("                       Loading Date View ..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_date()
                break

            # Switch to categoty view
            # Uppercase and lowercase entry accepted
            elif user_input.lower() == "c":
                print()
                typingPrint("                       Loading Category View ..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_category(expenses.get_all_values())
                break

            # Invalid input raises error
            else:
                raise ValueError("")
        except ValueError:
            print()
            typingPrint(
                "Invalid input: Please enter (m) to return to Main Menu "
                "or (d) to switch to Date View "
                "or (c) to switch to Category View.\n",
                Fore.RED)


def view_expenses():
    """
    Runs the expense view menu.
    Allows the user to select how they want to view their expenses.
    """
    # Loop repeats until valid inuput is received
    while True:
        print()
        print(Fore.CYAN + "                  ◇─◇──◇── VIEW EXPENSES ──◇──◇─◇"
              "\n")
        typingPrint("Please select one of the following options:\n")
        print()
        print("    1. View by Date")
        print("    2. View by Category")
        print("    3. View by Month")
        print("    4. Return to Main Menu")
        print()

        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # View by date
            if user_input == "1":
                print()
                typingPrint("                       Loading Date View...\n",
                            Fore.YELLOW)
                pause_and_clear()
                view_by_date()
                break

            # View by category
            elif user_input == "2":
                print()
                typingPrint("                       Loading Category View..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_category(expenses.get_all_values())
                break

            # View by month
            elif user_input == "3":
                print()
                typingPrint("                       Loading Month View..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_by_month(data)
                break

            # Return to main menu
            elif user_input == "4":
                print()
                return_to_main()
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint(
                "Invalid input: Please select one "
                "of the options (1-4).\n", Fore.RED)


# Main Menu Functions


def main_menu():
    """
    Runs the main menu of the program.
    Allows the user to navigate to one of two sub-menus.
    """
    # Loop repeats until valid inuput is received
    while True:
        print()
        print(Fore.CYAN + "                  ◇─◇──◇── MAIN MENU ──◇──◇─◇\n")
        typingPrint("Please select one of the following options:\n")
        print()
        print("    1. Add Expenses")
        print("    2. View Expenses")
        print("    3. Exit")
        print()

        # Try... except for exception / error handling
        try:
            user_input = input("> ")

            # Add Expenses
            if user_input == "1":
                print()
                typingPrint("                       Loading, please wait..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                add_expenses()
                break

            # View Expenses
            elif user_input == "2":
                print()
                typingPrint("                       Loading, please wait..."
                            "\n", Fore.YELLOW)
                pause_and_clear()
                view_expenses()
                break

            # Exit program
            elif user_input == "3":
                print()
                typingPrint("                       Exiting...\n", Fore.YELLOW)
                pause_and_clear()
                break

            # Invalid input raises error
            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint(
                "Invalid input: Please select one "
                "of the options (1-3).\n", Fore.RED)
            user_input = input("> ")


def return_to_main():
    """
    Clears the screen and returns to the main menu after a brief delay.
    """
    typingPrint("                       Loading Main Menu...\n", Fore.YELLOW)
    pause_and_clear()
    main_menu()


# Run the main function
welcome_screen()
main_menu()
