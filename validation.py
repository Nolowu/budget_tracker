from datetime import date
from decimal import Decimal, InvalidOperation

MAX_AMOUNT = Decimal("1000000000")

def parse_amount(raw):
    try:
        amount = Decimal(str(raw).strip())
    except (InvalidOperation, ValueError):
        raise ValueError("Enter a valid amount, such as 1500 or 15.50.")
    if not amount.is_finite() or amount <= 0:
        raise ValueError("Amount must be a finite number greater than zero.")
    if amount > MAX_AMOUNT:
        raise ValueError("That amount is too large.")
    if amount.as_tuple().exponent < -2:
        raise ValueError("Use at most 2 decimal places.")
    return int(amount * 100)

def parse_date(raw):
    try:
        return date.fromisoformat(str(raw).strip()).isoformat()
    except ValueError:
        raise ValueError("Enter a valid date in YYYY-MM-DD format.")

def get_amount(prompt):
    while True:
        try: return parse_amount(input(prompt))
        except ValueError as exc: print(exc)

def get_category(prompt):
    while True:
        value = input(prompt).strip()
        if not value: print("Category cannot be empty.")
        elif len(value) > 50: print("Category must be 50 characters or fewer.")
        else: return value

def get_date(prompt, default_today=True):
    while True:
        raw = input(prompt).strip()
        if not raw and default_today: return date.today().isoformat()
        try: return parse_date(raw)
        except ValueError as exc: print(exc)

def get_transaction_number(prompt, max_number):
    while True:
        raw = input(prompt).strip()
        if raw.isascii() and raw.isdigit() and 1 <= int(raw) <= max_number: return int(raw)
        print(f"Enter a whole number from 1 to {max_number}.")
