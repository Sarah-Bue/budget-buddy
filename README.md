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
    1. [Add Expenses](#add-expenses)
    2. [View Expenses](#view-expenses)
    3. [Future Features](#future-features)
3. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
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


[Back to top ⇧](#budget-buddy)

## Features

### Add Expenses

#### Input Validation

### View Expenses

#### View by Date

#### View by Category

#### View by Month

### Future Features

[Back to top ⇧](#budget-buddy)

## Technologies Used

### Languages

### Frameworks, Libraries, and Programs

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
