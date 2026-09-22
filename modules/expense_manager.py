import json
import os

from models.expense import Expense


class ExpenseManager:

    def __init__(self, file_path):
        self.file_path = file_path
        self.expenses = []

        directory = os.path.dirname(self.file_path)

        if directory:
            os.makedirs(
                directory,
                exist_ok=True
            )

        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(self.file_path):
            self.expenses = []
            return

        try:
            with open(
                self.file_path,
                "r"
            ) as file:
                data = json.load(file)

            self.expenses = [
                Expense.from_dict(item)
                for item in data
            ]

        except (
            json.JSONDecodeError,
            KeyError,
            TypeError
        ):
            print(
                "Warning: Could not read expense data."
            )
            self.expenses = []

    def save_expenses(self):
        try:
            with open(
                self.file_path,
                "w"
            ) as file:
                json.dump(
                    [
                        expense.to_dict()
                        for expense in self.expenses
                    ],
                    file,
                    indent=4
                )

        except OSError:
            print(
                "Error: Could not save expense data."
            )

    def generate_id(self):
        if not self.expenses:
            return 1

        return max(
            expense.expense_id
            for expense in self.expenses
        ) + 1

    def add_expense(
        self,
        amount,
        category,
        description,
        date
    ):
        expense = Expense(
            self.generate_id(),
            amount,
            category,
            description,
            date
        )

        self.expenses.append(expense)
        self.save_expenses()

        return expense

    def get_all_expenses(self):
        return self.expenses

    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                self.expenses.remove(expense)
                self.save_expenses()
                return True

        return False

    def search_expenses(self, keyword):
        keyword = keyword.lower()
        results = []

        for expense in self.expenses:
            if (
                keyword in expense.category.lower()
                or keyword in expense.description.lower()
                or keyword in expense.date.lower()
            ):
                results.append(expense)

        return results

    def get_total_spending(self):
        total = 0

        for expense in self.expenses:
            total += expense.amount

        return total
    