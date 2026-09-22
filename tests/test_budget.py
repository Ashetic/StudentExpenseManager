import unittest

from models.budget import Budget


class TestBudget(unittest.TestCase):

    def setUp(self):

        self.budget = Budget()

        self.budget.set_budget(
            "09-2026",
            10000
        )

    def test_set_budget(self):

        amount = self.budget.get_budget(
            "09-2026"
        )

        self.assertEqual(
            amount,
            10000
        )

    def test_remaining_budget(self):

        remaining = self.budget.get_remaining(
            "09-2026",
            4000
        )

        self.assertEqual(
            remaining,
            6000
        )

    def test_percentage_used(self):

        percentage = (
            self.budget.get_percentage_used(
                "09-2026",
                5000
            )
        )

        self.assertEqual(
            percentage,
            50
        )

    def test_budget_under_control(self):

        status = self.budget.get_status(
            "09-2026",
            5000
        )

        self.assertEqual(
            status,
            "Budget is under control."
        )

    def test_budget_warning(self):

        status = self.budget.get_status(
            "09-2026",
            8000
        )

        self.assertEqual(
            status,
            "Warning: You have used 80% or more of your budget."
        )

    def test_budget_exceeded(self):

        status = self.budget.get_status(
            "09-2026",
            12000
        )

        self.assertEqual(
            status,
            "Budget exceeded!"
        )

    def test_no_budget(self):

        status = self.budget.get_status(
            "10-2026",
            5000
        )

        self.assertEqual(
            status,
            "No budget has been set for this month."
        )


if __name__ == "__main__":
    unittest.main()
