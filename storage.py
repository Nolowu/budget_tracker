import json
from dataclasses import asdict
from datetime import date
from pathlib import Path
from uuid import uuid4
from model import Transaction

DATA_FILE = Path(__file__).parent / "data" / "transactions.json"

def save_transactions(transactions, path=DATA_FILE):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps([asdict(t) for t in transactions], indent=2), encoding="utf-8")
    temporary.replace(path)

def _valid(t):
    if t.type not in ("income", "expense"): return False
    if not isinstance(t.category, str) or not t.category.strip() or len(t.category) > 50: return False
    if type(t.amount) is not int or t.amount <= 0: return False
    if not isinstance(t.note, str): return False
    if not isinstance(t.transaction_id, str) or not t.transaction_id.strip(): return False
    try: date.fromisoformat(t.transaction_date)
    except (TypeError, ValueError): return False
    return True

def load_transactions(path=DATA_FILE):
    path = Path(path)
    try:
        raw = json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        legacy = path.parent.parent / "transactions.json"
        if path == DATA_FILE and legacy.exists():
            return load_transactions(legacy)
        return []
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Warning: could not read saved transactions ({exc}). Starting with an empty list.")
        return []
    if not isinstance(raw, list):
        print("Warning: saved transaction data must be a list. Starting with an empty list.")
        return []
    transactions = []
    for item in raw:
        if not isinstance(item, dict):
            print("Warning: skipped malformed transaction."); continue
        # Upgrade records from the earlier tracker format without losing them.
        item = dict(item)
        item.setdefault("note", "")
        item.setdefault("transaction_id", str(uuid4()))
        item.setdefault("transaction_date", date.today().isoformat())
        try: transaction = Transaction(**item)
        except (TypeError, ValueError):
            print("Warning: skipped malformed transaction."); continue
        if _valid(transaction): transactions.append(transaction)
        else: print("Warning: skipped invalid transaction.")
    return transactions

