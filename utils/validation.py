from datetime import datetime


def validate_amount(value):

    try:
        amount = float(value)

        if amount <= 0:
            return False, "Amount must be greater than zero."

        return True, amount

    except ValueError:
        return False, "Amount must be a valid number."


def validate_text(value, field_name):

    value = value.strip()

    if not value:
        return False, f"{field_name} cannot be empty."

    return True, value


def validate_date(date_string):

    date_string = date_string.strip()

    try:
        date_object = datetime.strptime(
            date_string,
            "%d-%m-%Y"
        )

        formatted_date = date_object.strftime(
            "%d-%m-%Y"
        )

        if date_string != formatted_date:
            return (
                False,
                "Date must be in DD-MM-YYYY format."
            )

        return True, formatted_date

    except ValueError:

        return (
            False,
            "Invalid date. Please use DD-MM-YYYY."
        )


def validate_month(month_string):

    month_string = month_string.strip()

    try:
        month_object = datetime.strptime(
            month_string,
            "%m-%Y"
        )

        formatted_month = month_object.strftime(
            "%m-%Y"
        )

        if month_string != formatted_month:
            return (
                False,
                "Month must be in MM-YYYY format."
            )

        return True, formatted_month

    except ValueError:

        return (
            False,
            "Invalid month. Please use MM-YYYY."
        )
    