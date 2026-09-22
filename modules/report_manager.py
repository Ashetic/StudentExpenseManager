class ReportManager:

    def __init__(self, expense_manager):
        self.expense_manager = expense_manager

    def get_monthly_expenses(self, month):

        expenses = (
            self.expense_manager.get_all_expenses()
        )

        monthly_expenses = []

        for expense in expenses:

            if expense.date[3:] == month:
                monthly_expenses.append(expense)

        return monthly_expenses

    def get_monthly_total(self, month):

        expenses = self.get_monthly_expenses(month)

        total = 0

        for expense in expenses:
            total += expense.amount

        return total

    def get_category_totals(self, month=None):

        if month:
            expenses = self.get_monthly_expenses(month)
        else:
            expenses = (
                self.expense_manager.get_all_expenses()
            )

        category_totals = {}

        for expense in expenses:

            category = expense.category

            if category not in category_totals:
                category_totals[category] = 0

            category_totals[category] += expense.amount

        return category_totals

    def get_highest_expense(self, month=None):

        if month:
            expenses = self.get_monthly_expenses(month)
        else:
            expenses = (
                self.expense_manager.get_all_expenses()
            )

        if not expenses:
            return None

        highest = expenses[0]

        for expense in expenses:

            if expense.amount > highest.amount:
                highest = expense

        return highest

    def get_lowest_expense(self, month=None):

        if month:
            expenses = self.get_monthly_expenses(month)
        else:
            expenses = (
                self.expense_manager.get_all_expenses()
            )

        if not expenses:
            return None

        lowest = expenses[0]

        for expense in expenses:

            if expense.amount < lowest.amount:
                lowest = expense

        return lowest

    def get_average_expense(self, month=None):

        if month:
            expenses = self.get_monthly_expenses(month)
        else:
            expenses = (
                self.expense_manager.get_all_expenses()
            )

        if not expenses:
            return 0

        total = 0

        for expense in expenses:
            total += expense.amount

        return total / len(expenses)

    def get_category_percentages(self, month=None):

        category_totals = self.get_category_totals(month)

        if month:
            total = self.get_monthly_total(month)
        else:
            total = (
                self.expense_manager.get_total_spending()
            )

        category_percentages = {}

        if total == 0:
            return category_percentages

        for category, amount in category_totals.items():

            percentage = (
                amount / total
            ) * 100

            category_percentages[category] = percentage

        return category_percentages
    
    