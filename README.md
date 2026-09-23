# Student Expense & Budget Management System

## 1. Project Overview

The Student Expense & Budget Management System is a Python-based
command-line application designed to help students record, manage,
search, and analyze their daily expenses.

The application also allows students to set monthly budgets and
monitor their spending against those budgets.

The project demonstrates important Python programming concepts such
as Object-Oriented Programming, modules, packages, file handling,
JSON data storage, exception handling, input validation, and unit
testing.

---

## 2. Objectives

The main objectives of this project are:

- To maintain a record of student expenses.
- To categorize expenses.
- To calculate total spending.
- To search and delete expenses.
- To manage monthly budgets.
- To calculate remaining monthly budget.
- To display budget usage percentage.
- To provide warnings when the budget is close to being exceeded.
- To generate expense reports.
- To analyze category-wise spending.
- To provide a modular and maintainable Python application.

---

## 3. Features

### Expense Management

The system allows users to:

- Add a new expense.
- View all expenses.
- Delete an expense.
- Search expenses.
- Calculate total spending.

### Monthly Budget Management

Users can:

- Set a budget for a specific month.
- View the budget for a month.
- Calculate remaining budget.
- Calculate budget usage percentage.
- Receive budget status messages.

### Expense Reports

The system provides:

- Monthly expense reports.
- Total monthly spending.
- Average expense.
- Highest expense.
- Lowest expense.
- Category-wise spending totals.
- Category-wise spending percentages.

### Data Storage

Expense and budget information is stored using JSON files.

The application automatically loads saved data when it starts.

---

## 4. Technologies Used

- Python 3
- JSON
- Object-Oriented Programming
- Python Standard Library
- unittest
- Command Line Interface

No external Python packages are required.

---

## 5. Python Concepts Demonstrated

This project demonstrates the following Python concepts:

### Variables and Data Types

The application uses strings, integers, floating-point numbers,
lists, dictionaries, and Boolean values.

### Conditional Statements

`if`, `elif`, and `else` statements are used for validation,
budget calculations, and menu operations.

### Loops

`for` and `while` loops are used for processing expenses and
displaying the interactive menu.

### Functions

Functions are used to divide application operations into smaller
and reusable tasks.

### Object-Oriented Programming

The project uses classes such as:

- `Expense`
- `Budget`
- `ExpenseManager`
- `BudgetManager`
- `ReportManager`

### Modules and Packages

The application is divided into multiple Python modules and
packages to improve organization and maintainability.

### File Handling

JSON files are used to permanently store application data.

### Exception Handling

`try` and `except` blocks are used to handle invalid data and
file-related errors.

### Input Validation

Reusable validation functions check amounts, text, dates, and
month formats.

### Unit Testing

Python's built-in `unittest` framework is used to test important
application functionality.

---

## 6. Project Structure

```text
StudentExpenseManager/
│
├── README.md
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
│
├── models/
│   ├── __init__.py
│   ├── expense.py
│   └── budget.py
│
├── modules/
│   ├── __init__.py
│   ├── expense_manager.py
│   ├── budget_manager.py
│   └── report_manager.py
│
├── utils/
│   ├── __init__.py
│   └── validation.py
│
├── data/
│   ├── expenses.json
│   └── budget.json
│
└── tests/
    ├── __init__.py
    ├── test_expense.py
    ├── test_budget.py
    ├── test_search.py
    └── test_report.py
    
    ## Web Application

The Student Expense & Budget Management System also includes a Flask-based web interface.

### Start the Web Application

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
