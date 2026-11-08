from decimal import Decimal, InvalidOperation

MAX_AMOUNT = Decimal("1000000000")


def get_category(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value:
            return value
        print("Category cannot be empty. Please try again.")


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