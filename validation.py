from decimal import Decimal, InvalidOperation

MAX_AMOUNT = Decimal("1000000000")


def get_category(prompt):
    while True:
        value = input(prompt).strip().lower()
        if not value:
            print("Category cannot be empty. Please try again.")
        elif not any(ch.isalpha() for ch in value):
            print("Category must contain at least one letter, e.g. food or rent.")
        elif len(value) > 30:
            print("Category is too long. Please use 30 characters or fewer.")
        else:
            return value


def get_transaction_number(prompt, max_number):
    while True:
        raw = input(prompt).strip()

        if not (raw.isascii() and raw.isdigit()):
            print("Please enter a whole number, for example 1.")
            continue

        number = int(raw)
        if number < 1 or number > max_number:
            print(f"Please enter a number from 1 to {max_number}.")
            continue

        return number


def get_amount(prompt):
    while True:
        raw = input(prompt).strip()

        try:
            amount = Decimal(raw)
        except InvalidOperation:
            print("Please enter a number, for example 1500 or 15.50.")
            continue

        if not amount.is_finite():
            print("Please enter a normal number.")
            continue
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        if amount > MAX_AMOUNT:
            print("That amount is too large.")
            continue
        if amount.as_tuple().exponent < -2:
            print("Use at most 2 decimal places.")
            continue

        return int(amount * 100)


if __name__ == "__main__":
    print(get_amount("Amount: "))