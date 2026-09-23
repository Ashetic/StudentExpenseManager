from flask import Flask, render_template, request, redirect, url_for

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


app = Flask(__name__)

expense_manager = ExpenseManager(EXPENSE_FILE)
budget_manager = BudgetManager(BUDGET_FILE)
report_manager = ReportManager(expense_manager)


@app.route("/")
def home():
    expenses = expense_manager.get_all_expenses()
    total_spending = expense_manager.get_total_spending()

    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        expenses=expenses,
        total_spending=total_spending,
        message=None,
        message_type=None
    )


@app.route("/add", methods=["POST"])
def add_expense():
    amount_input = request.form.get("amount", "")
    category_input = request.form.get("category", "")
    description_input = request.form.get("description", "")
    date_input = request.form.get("date", "")

    valid, amount = validate_amount(amount_input)

    if not valid:
        return render_home_message(
            amount,
            category_input,
            description_input,
            date_input
        )

    valid, category = validate_text(
        category_input,
        "Category"
    )

    if not valid:
        return render_home_message(
            amount_input,
            category_input,
            description_input,
            date_input,
            category
        )

    valid, description = validate_text(
        description_input,
        "Description"
    )

    if not valid:
        return render_home_message(
            amount_input,
            category_input,
            description_input,
            date_input,
            description
        )

    valid, date = validate_date(date_input)

    if not valid:
        return render_home_message(
            amount_input,
            category_input,
            description_input,
            date_input,
            date
        )

    expense_manager.add_expense(
        amount,
        category,
        description,
        date
    )

    return redirect(url_for("home"))


@app.route("/delete/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    expense_manager.delete_expense(expense_id)

    return redirect(url_for("home"))


@app.route("/search")
def search():
    keyword = request.args.get("keyword", "").strip()

    if keyword:
        expenses = expense_manager.search_expenses(keyword)
    else:
        expenses = expense_manager.get_all_expenses()

    total_spending = sum(
        expense.amount
        for expense in expenses
    )

    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        expenses=expenses,
        total_spending=total_spending,
        search_keyword=keyword,
        message=None,
        message_type=None
    )


@app.route("/budget", methods=["POST"])
def set_budget():
    month_input = request.form.get("month", "")
    amount_input = request.form.get("budget_amount", "")

    valid, month = validate_month(month_input)

    if not valid:
        return render_budget_message(
            month_input,
            amount_input,
            month
        )

    valid, amount = validate_amount(amount_input)

    if not valid:
        return render_budget_message(
            month_input,
            amount_input,
            amount
        )

    budget_manager.set_budget(
        month,
        amount
    )

    return redirect(
        url_for(
            "budget_status",
            month=month
        )
    )


@app.route("/budget-status")
def budget_status():
    month = request.args.get("month", "")

    valid, validated_month = validate_month(month)

    if not valid:
        return render_template(
            "index.html",
            app_name=APP_NAME,
            version=APP_VERSION,
            expenses=expense_manager.get_all_expenses(),
            total_spending=expense_manager.get_total_spending(),
            budget_month="",
            budget_amount=0,
            monthly_total=0,
            remaining=0,
            percentage=0,
            status=validated_month,
            message=validated_month,
            message_type="error"
        )

    monthly_total = report_manager.get_monthly_total(
        validated_month
    )

    budget_amount = budget_manager.get_budget(
        validated_month
    )

    remaining = budget_manager.get_remaining(
        validated_month,
        monthly_total
    )

    percentage = budget_manager.get_percentage_used(
        validated_month,
        monthly_total
    )

    status = budget_manager.get_status(
        validated_month,
        monthly_total
    )

    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        expenses=expense_manager.get_all_expenses(),
        total_spending=expense_manager.get_total_spending(),
        budget_month=validated_month,
        budget_amount=budget_amount,
        monthly_total=monthly_total,
        remaining=remaining,
        percentage=percentage,
        status=status,
        message=None,
        message_type=None
    )


@app.route("/reports")
def reports():
    month = request.args.get("month", "").strip()

    if month:
        valid, validated_month = validate_month(month)

        if not valid:
            return render_template(
                "index.html",
                app_name=APP_NAME,
                version=APP_VERSION,
                expenses=expense_manager.get_all_expenses(),
                total_spending=expense_manager.get_total_spending(),
                report_error=validated_month,
                message=None,
                message_type=None
            )

        monthly_total = report_manager.get_monthly_total(
            validated_month
        )

        category_totals = report_manager.get_category_totals(
            validated_month
        )

        highest = report_manager.get_highest_expense(
            validated_month
        )

        lowest = report_manager.get_lowest_expense(
            validated_month
        )

        average = report_manager.get_average_expense(
            validated_month
        )

        category_percentages = (
            report_manager.get_category_percentages(
                validated_month
            )
        )

        report_month = validated_month

    else:
        monthly_total = report_manager.get_monthly_total(
            ""
        )

        category_totals = report_manager.get_category_totals()

        highest = report_manager.get_highest_expense()

        lowest = report_manager.get_lowest_expense()

        average = report_manager.get_average_expense()

        category_percentages = (
            report_manager.get_category_percentages()
        )

        report_month = "All Time"

    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        expenses=expense_manager.get_all_expenses(),
        total_spending=expense_manager.get_total_spending(),
        report_month=report_month,
        report_total=monthly_total,
        category_totals=category_totals,
        category_percentages=category_percentages,
        highest=highest,
        lowest=lowest,
        average=average,
        message=None,
        message_type=None
    )


def render_home_message(
    amount,
    category,
    description,
    date,
    error_message="Invalid input."
):
    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        expenses=expense_manager.get_all_expenses(),
        total_spending=expense_manager.get_total_spending(),
        form_amount=amount,
        form_category=category,
        form_description=description,
        form_date=date,
        message=error_message,
        message_type="error"
    )


def render_budget_message(
    month,
    amount,
    error_message
):
    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        expenses=expense_manager.get_all_expenses(),
        total_spending=expense_manager.get_total_spending(),
        budget_month=month,
        budget_amount=amount,
        message=error_message,
        message_type="error"
    )


if __name__ == "__main__":
    app.run(
        debug=True
    )
    