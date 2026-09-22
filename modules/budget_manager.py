import json
import os

from models.budget import Budget


class BudgetManager:

    def __init__(self, file_path):

     self.file_path = file_path
     self.budget = Budget()

     directory = os.path.dirname(self.file_path)
    
     if directory:
        os.makedirs(
            directory,
            exist_ok=True
        )

     self.load_budget()

    def load_budget(self):

        if not os.path.exists(self.file_path):
            self.budget = Budget()
            return

        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)

            self.budget = Budget.from_dict(data)

        except (json.JSONDecodeError, TypeError, KeyError):
            print("Warning: Could not read budget data.")
            self.budget = Budget()

    def save_budget(self):

        try:

            with open(
            self.file_path,
            "w"
        ) as file:

                json.dump(
                self.budget.to_dict(),
                file,
                indent=4
            )

        except OSError:

         print(
            "Error: Could not save budget data."
        )

    def set_budget(self, month, amount):

        self.budget.set_budget(
            month,
            amount
        )

        self.save_budget()

    def get_budget(self, month):

        return self.budget.get_budget(month)

    def get_remaining(self, month, total_spending):

        return self.budget.get_remaining(
            month,
            total_spending
        )

    def get_percentage_used(
        self,
        month,
        total_spending
    ):

        return self.budget.get_percentage_used(
            month,
            total_spending
        )

    def get_status(self, month, total_spending):

        return self.budget.get_status(
            month,
            total_spending
        )
    