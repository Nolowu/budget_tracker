from datetime import date
from model import Transaction

def create_transaction(kind, category, amount, note="", transaction_date=None):
    if kind not in ("income", "expense"):
        raise ValueError("Transaction type must be income or expense.")
    if not isinstance(category, str) or not category.strip() or len(category) > 50:
        raise ValueError("Category must contain 1 to 50 characters.")
    if type(amount) is not int or amount <= 0:
        raise ValueError("Amount must be a positive integer number of minor currency units.")
    if not isinstance(note, str):
        raise ValueError("Description must be text.")
    transaction_date = transaction_date or date.today().isoformat()
    try: transaction_date = date.fromisoformat(transaction_date).isoformat()
    except (TypeError, ValueError): raise ValueError("Date must use YYYY-MM-DD format.")
    return Transaction(kind, category.strip(), amount, note.strip(), transaction_date=transaction_date)

def delete_transaction(transactions, transaction_id):
    for index, transaction in enumerate(transactions):
        if transaction.transaction_id == transaction_id:
            return transactions.pop(index)
    return None
