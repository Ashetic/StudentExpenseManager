import unittest

from models.expense import Expense


class TestExpense(unittest.TestCase):

    def setUp(self):
        self.expense = Expense(
            1,
            500.0,
            "Food",
            "Lunch",
            "20-09-2026"
        )

    def test_expense_creation(self):

        self.assertEqual(
            self.expense.expense_id,
            1
        )

        self.assertEqual(
            self.expense.amount,
            500.0
        )

        self.assertEqual(
            self.expense.category,
            "Food"
        )

        self.assertEqual(
            self.expense.description,
            "Lunch"
        )

        self.assertEqual(
            self.expense.date,
            "20-09-2026"
        )

    def test_to_dict(self):

        data = self.expense.to_dict()

        self.assertEqual(
            data["expense_id"],
            1
        )

        self.assertEqual(
            data["amount"],
            500.0
        )

        self.assertEqual(
            data["category"],
            "Food"
        )

    def test_from_dict(self):

        data = {
            "expense_id": 2,
            "amount": 1000.0,
            "category": "Education",
            "description": "Books",
            "date": "21-09-2026"
        }

        expense = Expense.from_dict(data)

        self.assertEqual(
            expense.expense_id,
            2
        )

        self.assertEqual(
            expense.amount,
            1000.0
        )

        self.assertEqual(
            expense.category,
            "Education"
        )


if __name__ == "__main__":
    unittest.main()
    