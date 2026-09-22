import json
import os
import tempfile
import unittest

from modules.expense_manager import ExpenseManager
from modules.report_manager import ReportManager


class TestReportManager(unittest.TestCase):

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

        self.expense_manager = ExpenseManager(
            self.temp_file.name
        )

        self.report_manager = ReportManager(
            self.expense_manager
        )

        self.expense_manager.add_expense(
            500,
            "Food",
            "Lunch",
            "20-09-2026"
        )

        self.expense_manager.add_expense(
            1000,
            "Transport",
            "Bus",
            "21-09-2026"
        )

        self.expense_manager.add_expense(
            1500,
            "Food",
            "Groceries",
            "22-09-2026"
        )

        self.expense_manager.add_expense(
            2000,
            "Education",
            "Books",
            "05-10-2026"
        )

    def tearDown(self):

        if os.path.exists(
            self.temp_file.name
        ):

            os.remove(
                self.temp_file.name
            )

    def test_monthly_expenses(self):

        expenses = (
            self.report_manager
            .get_monthly_expenses(
                "09-2026"
            )
        )

        self.assertEqual(
            len(expenses),
            3
        )

    def test_monthly_total(self):

        total = (
            self.report_manager
            .get_monthly_total(
                "09-2026"
            )
        )

        self.assertEqual(
            total,
            3000
        )

    def test_category_totals(self):

        category_totals = (
            self.report_manager
            .get_category_totals(
                "09-2026"
            )
        )

        self.assertEqual(
            category_totals["Food"],
            2000
        )

        self.assertEqual(
            category_totals["Transport"],
            1000
        )

    def test_highest_expense(self):

        highest = (
            self.report_manager
            .get_highest_expense(
                "09-2026"
            )
        )

        self.assertEqual(
            highest.amount,
            1500
        )

    def test_lowest_expense(self):

        lowest = (
            self.report_manager
            .get_lowest_expense(
                "09-2026"
            )
        )

        self.assertEqual(
            lowest.amount,
            500
        )

    def test_average_expense(self):

        average = (
            self.report_manager
            .get_average_expense(
                "09-2026"
            )
        )

        self.assertEqual(
            average,
            1000
        )

    def test_category_percentages(self):

        percentages = (
            self.report_manager
            .get_category_percentages(
                "09-2026"
            )
        )

        self.assertAlmostEqual(
            percentages["Food"],
            66.6666666667,
            places=2
        )

        self.assertAlmostEqual(
            percentages["Transport"],
            33.3333333333,
            places=2
        )

    def test_empty_month(self):

        expenses = (
            self.report_manager
            .get_monthly_expenses(
                "01-2026"
            )
        )

        self.assertEqual(
            len(expenses),
            0
        )


if __name__ == "__main__":
    unittest.main()
    