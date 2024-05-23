# Libraries
import datetime
import os
import sys
import time

import colorama
import gspread

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

# Tutorial and code: https://www.101computing.net/python-typing-text-effect/
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


# I don't think I'm using this let's see
# Tutorial and code: https://www.101computing.net/python-typing-text-effect/
""" def typingInput(text):

    Replaces input() with typingInput() to create typing effect.

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value """


def program_start():
    """
    Displays logo to welcome the user.
    """
    print()
    print(Fore.GREEN + '''
    ══════════════════════════════════════════════════════

    888888ba                 dP                     dP
    88    `8b                88                     88
   a88aaaa8P' dP    dP .d888b88 .d8888b. .d8888b. d8888P
    88   `8b. 88    88 88'  `88 88'  `88 88ooood8   88
    88    .88 88.  .88 88.  .88 88.  .88 88.  ...   88
    88888888P `88888P' `88888P8 `8888P88 `88888P'   dP
                                    .88


    888888ba                 dP       dP
    88    `8b                88       88
   a88aaaa8P' dP    dP .d888b88 .d888b88 dP    dP
    88   `8b. 88    88 88'  `88 88'  `88 88    88
    88    .88 88.  .88 88.  .88 88.  .88 88.  .88
    88888888P `88888P' `88888P8 `88888P8 `8888P88
                                            .88
                                        d8888P

    ══════════════════════════════════════════════════════
    ''')
    time.sleep(3)
    clearScreen()


# Add Expenses Menu Functions

def validate_expense_amount():
    """
    Validates user's expense amount input.
    While loop will repeatedly request data until it is valid.
    """
    typingPrint("Please enter an amount:\n")
    while True:
        try:
            # global so variable can be accessed in other functions
            global amount_input
            amount_input = float(input("> "))
            if amount_input != "":
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: Please enter a number.\n", Fore.RED)


def validate_expense_category():
    """
    Validate user's expense category input.
    While loop will repeatedly request data until it is valid.
    """
    # global so variable can be accessed in other functions
    global expense_categories
    expense_categories = [
        "Housing",
        "Food",
        "Transportation",
        "Entertainment",
        "Healthcare",
        "Misc"
    ]

    typingPrint("Please select a category (1-6).\n")

    while True:
        # Loop through each item in list and print it with corresponding number
        # +1 to display index as 1-6 rather than 0-5
        for i, expense_category in enumerate(expense_categories):
            print(f"    {i+1}. {expense_category}")

        try:
            # -1 to get "true" index number rather than displayed index number
            user_input = int(input("> ")) - 1
            if user_input in range(6):
                # global so variable can be accessed in other functions
                global category_input
                category_input = expense_categories[user_input]
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: "
                        "Please enter one of the options (1-6).\n", Fore.RED)


def validate_expense_description():
    """
    Validates user's expense description input.
    While loop will repeatedly request data until it is valid.
    """
    typingPrint("Please enter a description.\n")

    while True:
        try:
            # global so variable can be accessed in other functions
            global description_input
            description_input = input("> ")
            if description_input != "":
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: "
                        "Description cannot be empty.\n", Fore.RED)


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

            else:
                print()
                typingPrint("Invalid input: "
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
    typingPrint("Summarizing expenses...\n")
    time.sleep(1.5)
    clearScreen()
    print("══════════════════════════════════════════════════════")
    print()
    print(f"Your expense details:")
    print()
    print(f"     Expense Date: {date_input}")
    print(f"     Expense Description: {description_input}")
    print(f"     Expense Category: {category_input}")
    print(f"     Expense Amount: € {amount_input}")
    print()
    print("══════════════════════════════════════════════════════")
    print()
    typingPrint("Conrifm expense details (c) or re-enter (r)?\n")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == "r":
                time.sleep(1.5)
                clearScreen()
                add_expenses()

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

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Please enter (c) to confirm "
                        "or (r) to re-enter details.\n", Fore.RED)


def add_expenses():
    """
    Collects expense details from the user.
    After all data is collected and validated, a summary is shown to the user.
    """
    print(Fore.GREEN + "◇─◇──◇── ADD EXPENSES ──◇──◇─◇\n")
    typingPrint("Please add expense details below.\n")
    print()
    print("══════════════════════════════════════════════════════")
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
    typingPrint("Updating worksheet...\n")
    print()
    expenses_worksheet = SHEET.worksheet("expenses")
    expenses_worksheet.append_row(expense)
    typingPrint("Worksheet updated successfully.\n")
    print()
    typingPrint("Add another expense (a) or return to Main Menu (m)?\n")
    print()

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == "a":
                time.sleep(1.5)
                clearScreen()
                add_expenses()

            elif user_input.lower() == "m":
                print()
                typingPrint("Loading Main Menu...\n")
                time.sleep(1.5)
                clearScreen()
                main_menu()
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: "
                        "Please enter (a) to add another expense "
                        "or (m) to return to Main Menu.\n", Fore.RED)


# View Expenses Menu Functions

def calculate_total_expenses(data):
    """
    Calculates the sum of all expenses.
    """
    total_expenses = 0

    # Loops through each entry
    # Adds floats in 3rd index together
    for entry in data[1:]:
        total_expenses += float(entry[3])
    return total_expenses    


def view_by_category(data):
    """
    Calculates total expenses for each category.
    Displays categories in descending order.
    """
    category_totals = {}

    # Loop through data starting from index 1
    # Categories at index 2, amounts at index 3
    for entry in data[1:]:
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
    sorted_category_totals = dict(sorted(category_totals.items(),
                                         key=lambda item: item[1],
                                         reverse=True))

    total_expenses = calculate_total_expenses(data)

    print()
    print(Fore.GREEN + "◇─◇──◇── VIEW EXPENSES ──◇──◇─◇\n")
    print("Viewing Expenses by Category")
    print()
    print("══════════════════════════════════════════════════════\n")
    print()
    print(tabulate(sorted_category_totals.items(),
                   headers=["Category", "Total Expenses"]))
    print()
    print(f"                               Total Expenses: € {total_expenses}")
    print("══════════════════════════════════════════════════════\n")
    print()

    typingPrint("To return to Main Menu, please enter (m).\n")
    typingPrint("To switch to Date View, please enter (s).\n")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == "m":
                print()
                typingPrint("Loading Main Menu...\n")
                time.sleep(1.5)
                clearScreen()
                main_menu()
                break

            elif user_input.lower() == "s":
                print()
                typingPrint("Loading Date View...\n")
                time.sleep(1.5)
                clearScreen()
                view_by_date()
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: Please enter (m) "
                        "to return to Main Menu.\n", Fore.RED)


def view_by_date():
    """
    Displays expenses sorted by date.
    Allows user to return to main menu after viewing expenses.
    """

    total_expenses = calculate_total_expenses(data)

    print(Fore.GREEN + "◇─◇──◇── VIEW EXPENSES ──◇──◇─◇\n")
    print("Viewing Expenses by Date")

    #sort_by_date(data)

    # Adapted from: https://docs.python.org/3/library/datetime.html
    sorted_data = sorted(data[1:], key=lambda
                         x: datetime.datetime.strptime(x[0], "%d-%m-%Y"))

    print()
    print("══════════════════════════════════════════════════════\n")
    print()
    print(tabulate(sorted_data,
                   headers=[
                        "Date",
                        "Description",
                        "Category",
                        "Amount"
                    ]))
    print()
    print(f"                               Total Expenses: € {total_expenses}")
    print("══════════════════════════════════════════════════════\n")
    print()

    typingPrint("To return to Main Menu, please enter (m).\n")
    typingPrint("To switch to Category View, please enter (s).\n")

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == "m":
                print()
                typingPrint("Loading Main Menu...\n")
                time.sleep(1.5)
                clearScreen()
                main_menu()
                break

            elif user_input.lower() == "s":
                print()
                typingPrint("Loading Category View...\n")
                time.sleep(1.5)
                clearScreen()
                view_by_category(data)
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: Please enter (m) "
                        "to return to Main Menu.\n", Fore.RED)


def view_expenses():
    """
    Runs the expense view menu.
    Allows the user to select how they want to view their expenses.
    """
    while True:
        print()
        print(Fore.GREEN + "◇─◇──◇── VIEW EXPENSES ──◇──◇─◇\n")
        typingPrint("Please select one of the following options:\n")
        print()
        print("    1. View by Date")
        print("    2. View by Category")
        print("    3. Return to Main Menu")
        print()

        try:
            user_input = input("> ")
            if user_input == "1":
                print()
                typingPrint("Loading Date View...\n")
                time.sleep(1.5)
                clearScreen()
                view_by_date()
                break

            elif user_input == "2":
                print()
                typingPrint("Loading Category View...\n")
                time.sleep(1.5)
                clearScreen()
                view_by_category(expenses.get_all_values())
                break

            elif user_input == "3":
                print()
                typingPrint("Loading Main Menu...\n")
                time.sleep(1.5)
                clearScreen()
                main_menu()
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: Please select one "
                        "of the options (1-3).\n", Fore.RED)


# Main Menu Functions

def main_menu():
    """
    Runs the main menu of the program.
    Allows the user to navigate to one of two sub-menus.
    """
    while True:
        print()
        print(Fore.GREEN + "◇─◇──◇── MAIN MENU ──◇──◇─◇\n")
        typingPrint("Please select one of the following options:\n")
        print()
        print("    1. Add Expenses")
        print("    2. View Expenses")
        print("    3. Exit")
        print()

        try:
            user_input = input("> ")
            if user_input == "1":
                print()
                typingPrint("Loading...\n")
                time.sleep(1.5)
                clearScreen()
                add_expenses()
                break

            elif user_input == "2":
                print()
                typingPrint("Loading...\n")
                time.sleep(1.5)
                clearScreen()
                view_expenses()
                break

            elif user_input == "3":
                print()
                typingPrint("Exiting...\n")
                time.sleep(1.5)
                break

            else:
                raise ValueError("")

        except ValueError as e:
            print()
            typingPrint("Invalid input: Please select one "
                        "of the options (1-2).\n", Fore.RED)
            user_input = input("> ")


# Run the main function
#program_start()
#main_menu()
confirm_input()