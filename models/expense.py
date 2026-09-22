class Expense:
    def __init__(self, expense_id, amount, category, description, date):
        self.expense_id = expense_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def display_expense(self):
        print(f"ID          : {self.expense_id}")
        print(f"Amount      : ₹{self.amount:.2f}")
        print(f"Category    : {self.category}")
        print(f"Description : {self.description}")
        print(f"Date        : {self.date}")
        print("-" * 40)

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["expense_id"],
            data["amount"],
            data["category"],
            data["description"],
            data["date"]
        )