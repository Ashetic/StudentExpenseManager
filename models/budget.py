class Budget:
    def __init__(self, budgets=None):
        if budgets is None:
            budgets = {}

        self.budgets = budgets

    def set_budget(self, month, amount):
        self.budgets[month] = amount

    def get_budget(self, month):
        return self.budgets.get(month, 0)

    def get_remaining(self, month, total_spending):
        budget = self.get_budget(month)

        return budget - total_spending

    def get_percentage_used(self, month, total_spending):
        budget = self.get_budget(month)

        if budget == 0:
            return 0

        return (total_spending / budget) * 100

    def get_status(self, month, total_spending):
        budget = self.get_budget(month)

        if budget == 0:
            return "No budget has been set for this month."

        percentage = self.get_percentage_used(
            month,
            total_spending
        )

        if total_spending > budget:
            return "Budget exceeded!"

        elif percentage >= 80:
            return "Warning: You have used 80% or more of your budget."

        else:
            return "Budget is under control."

    def to_dict(self):
        return {
            "budgets": self.budgets
        }

    @staticmethod
    def from_dict(data):
        if "budgets" in data:
            return Budget(data["budgets"])

        # Compatibility with the old budget format
        if "amount" in data:
            return Budget({
                "09-2026": data["amount"]
            })

        return Budget()
    