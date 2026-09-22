from config import (
    APP_NAME,
    APP_VERSION,
    EXPENSE_FILE,
    BUDGET_FILE
)

from modules.expense_manager import ExpenseManager
from modules.budget_manager import BudgetManager
from modules.report_manager import ReportManager

from utils.validation import (
    validate_amount,
    validate_text,
    validate_date,
    validate_month
)

expense_manager = ExpenseManager(
    EXPENSE_FILE
)

budget_manager = BudgetManager(
    BUDGET_FILE
)

report_manager = ReportManager(
    expense_manager
)


def display_menu():

    print("\n")
    print("=" * 45)
    print(f"     {APP_NAME}")
    print(f"     Version {APP_VERSION}")
    print("=" * 45)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Search Expenses")
    print("5. Show Total Spending")
    print("6. Set Monthly Budget")
    print("7. View Budget Status")
    print("8. View Expense Reports")
    print("9. View Monthly Report")
    print("10. Exit")
    print("=" * 45)


def add_expense():

    print("\n--- Add Expense ---")

    amount_input = input(
        "Enter amount: ₹"
    ).strip()

    valid, result = validate_amount(
        amount_input
    )

    if not valid:
        print(result)
        return

    amount = result

    category_input = input(
        "Enter category: "
    )

    valid, result = validate_text(
        category_input,
        "Category"
    )

    if not valid:
        print(result)
        return

    category = result

    description_input = input(
        "Enter description: "
    )

    valid, result = validate_text(
        description_input,
        "Description"
    )

    if not valid:
        print(result)
        return

    description = result

    date_input = input(
        "Enter date (DD-MM-YYYY): "
    )

    valid, result = validate_date(
        date_input
    )

    if not valid:
        print(result)
        return

    date = result

    expense = expense_manager.add_expense(
        amount,
        category,
        description,
        date
    )

    print("\nExpense added successfully!")

    expense.display_expense()


def view_expenses():

    print("\n--- All Expenses ---")

    expenses = (
        expense_manager.get_all_expenses()
    )

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        expense.display_expense()

    print(
        f"Total Spending: "
        f"₹{expense_manager.get_total_spending():.2f}"
    )


def delete_expense():

    print("\n--- Delete Expense ---")

    try:

        expense_id = int(
            input(
                "Enter expense ID to delete: "
            )
        )

    except ValueError:

        print("Please enter a valid ID.")
        return

    deleted = (
        expense_manager.delete_expense(
            expense_id
        )
    )

    if deleted:

        print(
            "Expense deleted successfully."
        )

    else:

        print(
            "Expense ID not found."
        )


def search_expenses():

    print("\n--- Search Expenses ---")

    keyword = input(
        "Enter category, description or date: "
    ).strip()

    if not keyword:

        print(
            "Search keyword cannot be empty."
        )

        return

    results = (
        expense_manager.search_expenses(
            keyword
        )
    )

    if not results:

        print(
            "No matching expenses found."
        )

        return

    print(
        f"\nFound {len(results)} expense(s):\n"
    )

    for expense in results:
        expense.display_expense()


def set_budget():

    print("\n--- Set Monthly Budget ---")

    month_input = input(
        "Enter month (MM-YYYY): "
    ).strip()

    valid, result = validate_month(
        month_input
    )

    if not valid:

        print(result)
        return

    month = result

    amount_input = input(
        "Enter monthly budget: ₹"
    ).strip()

    valid, result = validate_amount(
        amount_input
    )

    if not valid:

        print(result)
        return

    amount = result

    budget_manager.set_budget(
        month,
        amount
    )

    print(
        f"\nBudget for {month} "
        f"set to ₹{amount:.2f}"
    )


def view_budget():

    print("\n--- Monthly Budget Status ---")

    month_input = input(
        "Enter month (MM-YYYY): "
    ).strip()

    valid, result = validate_month(
        month_input
    )

    if not valid:

        print(result)
        return

    month = result

    budget = budget_manager.get_budget(
        month
    )

    total_spending = (
        report_manager.get_monthly_total(
            month
        )
    )

    if budget == 0:

        print(
            f"No budget has been set for {month}."
        )

        print(
            f"Monthly Spending: "
            f"₹{total_spending:.2f}"
        )

        return

    remaining = budget_manager.get_remaining(
        month,
        total_spending
    )

    percentage = (
        budget_manager.get_percentage_used(
            month,
            total_spending
        )
    )

    status = budget_manager.get_status(
        month,
        total_spending
    )

    print(
        f"\nMonth          : {month}"
    )

    print(
        f"Monthly Budget : "
        f"₹{budget:.2f}"
    )

    print(
        f"Total Spent    : "
        f"₹{total_spending:.2f}"
    )

    print(
        f"Remaining      : "
        f"₹{remaining:.2f}"
    )

    print(
        f"Budget Used    : "
        f"{percentage:.2f}%"
    )

    print(
        f"Status         : "
        f"{status}"
    )


def view_reports():

    print("\n--- Expense Reports ---")

    expenses = (
        expense_manager.get_all_expenses()
    )

    if not expenses:

        print(
            "No expenses available for reporting."
        )

        return

    print("\nCategory-wise Spending")
    print("-" * 40)

    category_totals = (
        report_manager.get_category_totals()
    )

    for category, amount in (
        category_totals.items()
    ):

        print(
            f"{category:<20} : "
            f"₹{amount:.2f}"
        )

    print("\nCategory Percentages")
    print("-" * 40)

    category_percentages = (
        report_manager.get_category_percentages()
    )

    for category, percentage in (
        category_percentages.items()
    ):

        print(
            f"{category:<20} : "
            f"{percentage:.2f}%"
        )

    highest = (
        report_manager.get_highest_expense()
    )

    print("\nHighest Expense")
    print("-" * 40)

    print(
        f"Amount      : "
        f"₹{highest.amount:.2f}"
    )

    print(
        f"Category    : "
        f"{highest.category}"
    )

    print(
        f"Description : "
        f"{highest.description}"
    )

    print(
        f"Date        : "
        f"{highest.date}"
    )

    lowest = (
        report_manager.get_lowest_expense()
    )

    print("\nLowest Expense")
    print("-" * 40)

    print(
        f"Amount      : "
        f"₹{lowest.amount:.2f}"
    )

    print(
        f"Category    : "
        f"{lowest.category}"
    )

    print(
        f"Description : "
        f"{lowest.description}"
    )

    print(
        f"Date        : "
        f"{lowest.date}"
    )

    average = (
        report_manager.get_average_expense()
    )

    print("\nAverage Expense")
    print("-" * 40)

    print(
        f"Average     : "
        f"₹{average:.2f}"
    )

    print("\nTotal Spending")
    print("-" * 40)

    total = (
        expense_manager.get_total_spending()
    )

    print(
        f"Total       : "
        f"₹{total:.2f}"
    )


def view_monthly_report():

    print("\n--- Monthly Expense Report ---")

    month_input = input(
        "Enter month (MM-YYYY): "
    ).strip()

    valid, result = validate_month(
        month_input
    )

    if not valid:

        print(result)
        return

    month = result

    expenses = (
        report_manager.get_monthly_expenses(
            month
        )
    )

    if not expenses:

        print(
            f"No expenses found for {month}."
        )

        return

    print(
        f"\nExpenses for {month}"
    )

    print("-" * 45)

    for expense in expenses:

        expense.display_expense()

    total = (
        report_manager.get_monthly_total(
            month
        )
    )

    average = (
        report_manager.get_average_expense(
            month
        )
    )

    highest = (
        report_manager.get_highest_expense(
            month
        )
    )

    lowest = (
        report_manager.get_lowest_expense(
            month
        )
    )

    print("\nMonthly Summary")
    print("-" * 45)

    print(
        f"Total Spending : "
        f"₹{total:.2f}"
    )

    print(
        f"Average Expense: "
        f"₹{average:.2f}"
    )

    print(
        f"Highest Expense: "
        f"₹{highest.amount:.2f}"
    )

    print(
        f"Lowest Expense : "
        f"₹{lowest.amount:.2f}"
    )

    print("\nCategory-wise Spending")
    print("-" * 45)

    category_totals = (
        report_manager.get_category_totals(
            month
        )
    )

    for category, amount in (
        category_totals.items()
    ):

        print(
            f"{category:<20} : "
            f"₹{amount:.2f}"
        )


def main():

    while True:

        display_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            delete_expense()

        elif choice == "4":

            search_expenses()

        elif choice == "5":

            total = (
                expense_manager
                .get_total_spending()
            )

            print(
                f"\nTotal Spending: "
                f"₹{total:.2f}"
            )

        elif choice == "6":

            set_budget()

        elif choice == "7":

            view_budget()

        elif choice == "8":

            view_reports()

        elif choice == "9":

            view_monthly_report()

        elif choice == "10":

            print(
                "\nThank you for using "
                "Student Expense Manager!"
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-10."
            )


if __name__ == "__main__":
    main()
