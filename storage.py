import json
from dataclasses import asdict
from pathlib import Path

from model import Transaction

DATA_FILE = Path(__file__).parent / "transactions.json"


def save_transactions(transactions, path=DATA_FILE):
    data = [asdict(t) for t in transactions]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def is_valid(t):
    return (
        t.type in ("income", "expense")
        and isinstance(t.category, str)
        and t.category.strip() != ""
        and isinstance(t.amount, int)
        and t.amount > 0
    )


def load_transactions(path=DATA_FILE):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError):
        print("Warning: saved data is damaged. Keeping a backup and starting fresh.")
        try:
            path.replace(path.with_name(path.name + ".bak"))
        except OSError:
            pass
        return []

    if not isinstance(data, list):
        print("Warning: saved data has the wrong format. Starting fresh.")
        return []

    transactions = []
    for item in data:
        try:
            t = Transaction(**item)
        except TypeError:
            print("Warning: skipped a damaged record.")
            continue
        if is_valid(t):
            transactions.append(t)
        else:
            print("Warning: skipped an invalid record.")
    return transactions