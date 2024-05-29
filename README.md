# Budget Buddy

![Mock Up Image](/assets/readme-files/mockup.png)

Budget Buddy is a Python command line interface (CLI) application designed to help users manage their finances. Users can input their expenses and choose from a variety of views to break down their spending habits.

The program automatically syncs all inputs to a Google Sheet to ensure storage of and access to the expense details even outside of Budget Buddy.

Visit the deployed application [here](https://budget-buddy-expense-tracker-f207bb189dc1.herokuapp.com/).

## Table of Contents
1. [User Experience (UX)](#user-experience-ux)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Design Choices](#design-choices)
    4. [Data Model](#data-model)
    5. [Flowchart](#flowchart)
2. [Features](#features)
    1. [Program Start and Main Menu](#program-start-and-main-menu)
    2. [Add Expenses](#add-expenses)
    3. [View Expenses](#view-expenses)
    4. [Input Validation](#input-validation)
    5. [Future Features](#future-features)
3. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks, Libraries and Packages](#frameworks-libraries-and-packages)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Validation](#validation)
    3. [Manual Testing](#manual-testing)
    4. [Bugs](#bugs)
5. [Deployment](#deployment)
    1. [Connecting Google Sheet](#connecting-google-sheet)
    2. [Heroku](#heroku)
6. [Credits](#credit)
    1. [Content](#content)
    2. [Media](#media)
    3. [Code](#code)
7. [Acknowledgements](#acknowledgements)

## User Experience (UX)

### Project Goals

- The program should be easy to use.
- The program should provide users with feedback about their input.
- The program should allow users to add new expenses.
- The program should allow users to view existing expenses.
- The program should validate all user inputs.

### User Stories

- As a user, I want to be able to track and categorize my expenses.
- As a user, I want to be able to store my expense details in a Google Sheet for further processing.
- As a user, I want to be able to view my expenses in a convenient format.
- As a user, I want to be sure that my expense details are valid.
- As a user, I want the program to be pleasant and engaging.
- As a user, I want to receive feedback on my input.

### Design Choices

#### Color Scheme

Since this program is purely focussed on back-end programming, no additional styling or formatting was applied to the page that contains the terminal.

[Colorama](https://pypi.org/project/colorama/) was used to apply color to the terminal text to enhance the user experience.

The following colors were used:

- Error messages display in red.

- A successful feedback message about updating the Google Sheet displays in green.

- Menu headers and the program logo display in cyan.

All colors are displayed in the *normal* style on a *normal* background.

<details>
<summary> Colorama Palette </summary>
<img src = "assets/readme-files/colorama-palette.png")>
</details>

#### Banners and Logo

In order to improve the user's experience and enhance the visual appeal of the program, ASCII art was used to create a logo and header elements:

- [Many Tools](https://manytools.org/hacker-tools/ascii-banner/) was used to create the logo that displays when the program starts.

- [Emojicombos](https://emojicombos.com/deco-ascii-art) was used to create decorative menu headers.

#### Expense Display

To allow users to easily review and compare their potentially large number of expenses, these are displayed in a variety of tables, depending on the option the user selects.

[Tabulate](https://pypi.org/project/tabulate/) was used to create the tables used to display the expense details.

### Data Model

All user inputs are stored in a [Google Sheet](https://www.google.com/sheets/about/).

<details>
<summary> Google Sheet </summary>
<img src = "assets/readme-files/google-sheet.png")>
</details>

### Flowchart

During the initial planning phase, [Lucidchart](https://www.lucidchart.com/) was used to create a flowchart for the program to ensure a clear path for the user when navigating the menu.

<details>
<summary> Flowchart </summary>
<img src = "assets/readme-files/flowchart.png")>
</details>
<br>

[Back to top ⇧](#budget-buddy)

## Features

### General

- A loading screen message provides users with feedback when switching between menus or accessing the Google Sheet.
- A typing effect was added to input requests, error messages, and menu overviews (but not the individual menu items) to simulate human interaction and enhance engagement and readability.
- When switching between menus or between expense views, the screen is cleared to provice users with a cleaner display and improve readability and focus.
- A menu header at the top of the terminal provides the user with guidance on which menu they are currently in.

### Program Start and Main Menu

- After the opening screen of Budget Buddy's ASCII art banner, the main menu is loaded. From here, users can choose between adding new expenses or viewing existing expenses. Users may also choose to exit the program from the main screen.
- A colorful banner at the top provides users with guidance on where they are. 

<details>
<summary>Logo</summary>
<img src = "assets/readme-files/logo.png">
</details>

<details>
<summary>Main Menu</summary>
<img src = "assets/readme-files/main-menu.png">
</details>  

### Add Expenses

- The program collects various details from the user for each new expense, namely date, description, category, and amount.
- Each detail is collected using a new prompt and validated before users can proceed to the next detail.
-  Error messages inform users of incorrect inputs.
- After all details have been completed, users are shown a summary of their expense details. 
- Users can chose to confirm their inputs, saving them to the Google Sheet, or to re-enter them if they need to make any changes.
- After an expense has been added, users can choose to add another expense, which will re-start the process from the first step, or to return to the main menu.

<details>
<summary>Add Expense Details</summary>
<img src = "assets/readme-files/add-expense-details.png">
</details>  

<details>
<summary>Confirm Expense Details</summary>
<img src = "assets/readme-files/confirm-expense-details.png">
</details>  

### View Expenses

- The program offers several viewing methods: by date, by category, and by month.
- Expenses are displayed in tabulated form for ease of readability and comparison.
- Users can switch between different viewing modes and also return to the main menu from any view.
- Each viewing mode includes a total of all expenses at the bottom.

<details>
<summary>View Expenses Menu</summary>
<img src = "assets/readme-files/view-expenses-menu.png">
</details>  

#### View by Date

- In this view, all expenses are organized by date, from oldest to newest.
- The order of the columns reflects the order of the expense details users enter in the *Add Expenses* menu to maintain coherence.

<details>
<summary>Date View</summary>
<img src = "assets/readme-files/date-view.png">
</details>  

#### View by Category

- In this view, all expenses are displayed by category.
- The order of the categories reflects the order in which the categories were displayed in the *Add Expenses* menu to maintain coherence.

<details>
<summary>Category View</summary>
<img src = "assets/readme-files/category-view.png">
</details>  

#### View by Month

- In this view, all expenses are displayed by month and category.
- The months are marked in the left-most vertical column and are displayed in chronological order.
- The categories are marked along the header row and are displayed in the same order as they were in the *Add Expenses* menu to maintain coherence.
- A total row was added as the right-most vertical row to show totals per category per month.
- Abbrviated versions of the category names were used in the header row to allow for for easier reading and to fit within the confines of a compact table layout

<details>
<summary>Month View</summary>
<img src = "assets/readme-files/month-view.png">
</details>  

### Input Validation

- Input validation is performed every time users provide input.
- Before each input, users are given information on what kind of input is needed.
- In case of invalid input, an error message is printed in red, and users are reminded of what input types are accepted.
- After that, users will be able to provide input again.
- This loop will repeat until the program receives valid input.
- Where single letter inputs are required, both uppercase and lowecase letters will be accepted.
- Inputs cannot be empty.
- Dates are limited from 01-01-2024 to today and must be in DD-MM-YYYY format.
- Amounts have to be entered as numbers.

<details>
<summary>Input Validation</summary>
<img src = "assets/readme-files/input-validation.png">
</details>  

### Future Features

#### Category Totals for Month View

- A *total* column is provided at the end of the *Month View* to allow users to easily compare their total expenses by month.
- Adding a *total* row that displays the total expenses per category to date below the last month will provide additional insights into their spending habits to users.

#### Income Functionality

- To gain a more complete insight into their financial situation and allow for better planning, users will be able to add and view income details in addition to expense details.
- This would add a display of the remaining budget in each expense view, allowing users to plan their spending accordingly.
- Color coding could be added to provide feedback on over- or underspending.

#### Personalization

- In a new menu, users will be asked to define their own income and expense categories, rather than pick from a predefined list.
- Users will be able to set monthly and / or category budgets.

#### GUI

- Frameworks such as Tkinter and PyQt can be used to build graphical user interfaces for Python.
- A GUI would allow for a more user-friendly and visually appealing display of the program, improving the user experience.

#### Google Sheets Functionality

- Currently, Google Sheets is only used to store the expense details.
- By adding simple functionality such as charts and tables to the sheet, users would be able to view their expense details in a more appealing and accessible format.
- Google Sheets even allows for the possibility of interactive financial dashboards which would provide users with an engaging, easy to understand overview of their finances, based on their inputs into the expense and input tracker.

[Back to top ⇧](#budget-buddy)

## Technologies Used

### Languages

- [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))

Provided as part of Code Institute's [Python Essentials template](https://github.com/Code-Institute-Org/python-essentials-template): 
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [Javascript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries, and Packages

- [Colorama](https://pypi.org/project/colorama/) was used to add colour to the terminal.

- [Datetime](https://docs.python.org/3/library/datetime.html) was used to validate date inputs.

-[Defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict) was used to create a dictionary for expense categories and their corresponding totals.

- [Emojicombos](https://emojicombos.com/deco-ascii-art) was used to create decorative menu headers.

- [GitHub](https://github.com/) was used to store the project and for version control.

- [GitPod](https://gitpod.io/) was used for writing code, committing, and then pushing to GitHub.

- [GSpread](https://docs.gspread.org/en/v6.0.0/) was used to interact with the data in the linked sheet.

- [Google OAuth](https://google-auth.readthedocs.io/en/master/reference/google.oauth2.service_account.html) was used to authenticate the program in order to access Google's APIs.

- [Google Cloud](https://cloud.google.com/) was used to generate the APIs required to connect the data sheets with the Python code.

- [Google Sheets](https://docs.google.com/spreadsheets/) was used to store user input data.

- [Heroku](https://dashboard.heroku.com/login) was used to host and deploy the finished project.

- [Lucidchart](https://www.lucidchart.com/pages/) was used to create the flowchart during project planning.

- [Many Tools](https://manytools.org/hacker-tools/ascii-banner/) was used to create a logo for the program.

- [PEP8 online check](http://pep8online.com/) was used to validate the Python code.

- [Tabulate](https://pypi.org/project/tabulate/) was used to display the expense data in tables. 

- [Time](https://docs.python.org/3/library/time.html) was used to create delays in the program when switching between menus or performing operations. 

- [Sys](https://docs.python.org/3/library/sys.html) was used to create the typing effect on certain text outputs.

- [Os](https://docs.python.org/3/library/os.html) was used to clear the screen when switching between menus or views. 

[Back to top ⇧](#budget-buddy)

## Testing

### Testing User Stories

### Validation

#### Code Validation

#### User Input Validation

### Feature Testing

### Bugs

[Back to top ⇧](#budget-buddy)

## Deployment

### Connecting Google Sheet

### Heroku

[Back to top ⇧](#budget-buddy)


## Credits

[Back to top ⇧](#budget-buddy)


### Code

### Media

### Content

[Back to top ⇧](#budget-buddy)

## Acknowledgements

[Back to top ⇧](#budget-buddy)
