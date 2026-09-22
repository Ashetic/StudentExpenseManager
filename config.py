import os


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

EXPENSE_FILE = os.path.join(
    DATA_DIR,
    "expenses.json"
)

BUDGET_FILE = os.path.join(
    DATA_DIR,
    "budget.json"
)

APP_NAME = "Student Expense Manager"
APP_VERSION = "1.0.0"
