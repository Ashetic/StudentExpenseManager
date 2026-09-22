import json
import os
import tempfile
import unittest

from modules.expense_manager import ExpenseManager


class TestExpenseManager(unittest.TestCase):

    def setUp(self):

        self.temp_file = tempfile.NamedTemporaryFile(
            delete=False
        )

        self.temp_file.close()

        with open(
            self.temp_file.name,
            "w"
        ) as file:

            json.dump([], file)

        self.manager = ExpenseManager(
            self.temp_file.name
        )

    def tearDown(self):

        if os.path.exists(
            self.temp_file.name
        ):

            os.remove(
                self.temp_file.name
            )

    def test_add_expense(self):

        expense = self.manager.add_expense(
            500,
            "Food",
            "Lunch",
            "20-09-2026"
        )

        self.assertEqual(
            expense.expense_id,
            1
        )

        self.assertEqual(
            len(
                self.manager.get_all_expenses()
            ),
            1
        )

    def test_total_spending(self):

        self.manager.add_expense(
            500,
            "Food",
            "Lunch",
            "20-09-2026"
        )

        self.manager.add_expense(
            1000,
            "Transport",
            "Bus",
            "21-09-2026"
        )

        total = (
            self.manager.get_total_spending()
        )

        self.assertEqual(
            total,
            1500
        )

    def test_search_by_category(self):

        self.manager.add_expense(
            500,
            "Food",
            "Lunch",
            "20-09-2026"
        )

        self.manager.add_expense(
            1000,
            "Transport",
            "Bus",
            "21-09-2026"
        )

        results = (
            self.manager.search_expenses(
                "food"
            )
        )

        self.assertEqual(
            len(results),
            1
        )

        self.assertEqual(
            results[0].category,
            "Food"
        )

    def test_search_by_description(self):

        self.manager.add_expense(
            500,
            "Food",
            "College Lunch",
            "20-09-2026"
        )

        results = (
            self.manager.search_expenses(
                "college"
            )
        )

        self.assertEqual(
            len(results),
            1
        )

        self.assertEqual(
            results[0].description,
            "College Lunch"
        )

    def test_search_by_date(self):

        self.manager.add_expense(
            500,
            "Food",
            "Lunch",
            "20-09-2026"
        )

        results = (
            self.manager.search_expenses(
                "20-09-2026"
            )
        )

        self.assertEqual(
            len(results),
            1
        )

    def test_delete_expense(self):

        self.manager.add_expense(
            500,
            "Food",
            "Lunch",
            "20-09-2026"
        )

        deleted = (
            self.manager.delete_expense(1)
        )

        self.assertTrue(deleted)

        self.assertEqual(
            len(
                self.manager.get_all_expenses()
            ),
            0
        )

    def test_delete_nonexistent_expense(self):

        deleted = (
            self.manager.delete_expense(999)
        )

        self.assertFalse(deleted)


if __name__ == "__main__":
    unittest.main()
    