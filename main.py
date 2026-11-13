from reports import filter_transactions
from model import Transaction
from summary import balance, total, totals_by_category
from transactions import create_transaction, delete_transaction as remove_transaction
from storage import DATA_FILE, load_transactions, save_transactions
from validation import get_amount, get_category, get_date, get_transaction_number, parse_amount

transactions = load_transactions()
if not DATA_FILE.exists():
    save_transactions(transactions)

def money(minor_units):
    sign = "-" if minor_units < 0 else ""
    amount = abs(minor_units)
    return f"{sign}{amount // 100:,}.{amount % 100:02d}"

def show_menu():
    print("\n=== Budget Management System ===")
    for line in ("1. Add Income", "2. Add Expense", "3. View All Transactions", "4. Search Transactions", "5. Delete Transaction", "6. View Income Summary", "7. View Expense Summary", "8. View Category Reports", "9. View Available Balance", "10. Exit"):
        print(line)

def persist():
    try: save_transactions(transactions)
    except OSError as exc: print(f"Could not save transactions: {exc}")

def show_transactions(items):
    if not items:
        print("No transactions found."); return
    for index, t in enumerate(items, 1):
        sign = "+" if t.type == "income" else "-"
        print(f"{index}. {t.transaction_date} | {sign}{money(t.amount)} | {t.type.title()} | {t.category} | {t.note or '(no description)'} | ID: {t.transaction_id}")

def add_transaction(kind):
    print(f"\n--- Add {kind.title()} ---")
    category = get_category("Category: ")
    amount = get_amount("Amount: ")
    note = input("Description (optional): ").strip()
    transaction_date = get_date("Date (YYYY-MM-DD, blank for today): ")
    t = create_transaction(kind, category, amount, note, transaction_date)
    transactions.append(t); persist()
    print(f"Saved {kind}: {money(amount)} in {category} (ID {t.transaction_id}).")

def search_transactions():
    print("Leave filters blank to skip them.")
    kind = input("Type (income/expense): ").strip().lower() or None
    if kind not in (None, "income", "expense"):
        print("Type must be income or expense."); return
    category = input("Category: ").strip() or None
    day = input("Date (YYYY-MM-DD): ").strip() or None
    try:
        low_raw = input("Minimum amount (blank to skip): ").strip()
        low = parse_amount(low_raw) if low_raw else None
        high_raw = input("Maximum amount (blank to skip): ").strip()
        high = parse_amount(high_raw) if high_raw else None
        if low is not None and high is not None and low > high: raise ValueError("Minimum amount cannot exceed maximum amount.")
        results = filter_transactions(transactions, kind, category, day, low, high)
    except ValueError as exc:
        print(f"Invalid filter: {exc}"); return
    print("\n--- Search results ---"); show_transactions(results)

def delete_transaction():
    if not transactions:
        print("No transactions to delete."); return
    show_transactions(transactions)
    index = get_transaction_number("Transaction number to delete: ", len(transactions)) - 1
    chosen = transactions[index]
    answer = input(f"Delete {chosen.transaction_id} ({chosen.category}, {money(chosen.amount)})? (y/n): ").strip().lower()
    if answer in ("y", "yes"):
        remove_transaction(transactions, chosen.transaction_id); persist(); print("Transaction deleted.")
    else: print("Cancelled.")

def print_breakdown(title, kind):
    print(f"\n{title}")
    totals = totals_by_category(transactions, kind)
    if not totals: print("  (none)")
    for category, amount in sorted(totals.items(), key=lambda row: row[0].casefold()):
        print(f"  {category}: {money(amount)}")
    print(f"Total {kind}: {money(sum(totals.values()))}")

def main():
    actions = {"1": lambda: add_transaction("income"), "2": lambda: add_transaction("expense"), "3": lambda: show_transactions(transactions), "4": search_transactions, "5": delete_transaction, "6": lambda: print_breakdown("Income by category", "income"), "7": lambda: print_breakdown("Expenses by category", "expense"), "8": lambda: (print_breakdown("Income by category", "income"), print_breakdown("Expenses by category", "expense")), "9": lambda: print(f"Available balance: {money(balance(transactions))}")}
    while True:
        show_menu()
        choice = input("Choose an option (1-10): ").strip()
        if choice == "10": print("Goodbye!"); return
        action = actions.get(choice)
        if action is None: print("Invalid choice. Enter a number from 1 to 10."); continue
        try: action()
        except (EOFError, KeyboardInterrupt): raise
        except Exception as exc: print(f"Operation failed: {exc}")

if __name__ == "__main__":
    try: main()
    except (KeyboardInterrupt, EOFError): print("\nGoodbye!")




