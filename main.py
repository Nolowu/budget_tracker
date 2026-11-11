from model import Transaction
from validation import get_amount, get_category, get_transaction_number
from summary import totals_by_category, total, balance
from storage import load_transactions, save_transactions

transactions = load_transactions()


def format_money(cents):
    sign = "-" if cents < 0 else ""
    cents = abs(cents)
    return f"{sign}{cents // 100:,}.{cents % 100:02d}"


def show_menu():
    print("\n=== Student Budget Tracker ===")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all transactions")
    print("4. View summary")
    print("5. Delete a transaction")
    print("6. Quit")


def save_data():
    try:
        save_transactions(transactions)
    except OSError:
        print("Warning: could not write to the data file.")


def add_transaction(kind):
    print(f"\n--- Add {kind} ---")
    category = get_category("Category (e.g. food, rent, salary): ")
    amount = get_amount("Amount: ")
    note = input("Note (optional): ").strip()

    transactions.append(Transaction(kind, category, amount, note))
    print(f"Saved: {kind} of {format_money(amount)} in '{category}'.")
    save_data()


def view_transactions():
    print("\n--- All transactions ---")
    if not transactions:
        print("No transactions yet.")
        return

    for number, t in enumerate(transactions, start=1):
        sign = "+" if t.type == "income" else "-"
        print(f"{number}. {sign}{format_money(t.amount)}  {t.category}  {t.note}")


def delete_transaction():
    if not transactions:
        print("\nNo transactions to delete.")
        return

    view_transactions()
    number = get_transaction_number("Number to delete: ", len(transactions))

    t = transactions[number - 1]
    sign = "+" if t.type == "income" else "-"
    print(f"You chose: {sign}{format_money(t.amount)}  {t.category}  {t.note}")

    answer = input("Delete this transaction? (y/n): ").strip().lower()
    if answer in ("y", "yes"):
        transactions.pop(number - 1)
        save_data()
        print("Transaction deleted.")
    else:
        print("Cancelled. Nothing was deleted.")


def print_totals(title, totals):
    print(f"\n{title}")
    if not totals:
        print("  (none)")
        return
    for category, cents in sorted(totals.items()):
        print(f"  {category}: {format_money(cents)}")


def view_summary():
    print("\n--- Summary ---")
    print_totals("Income by category:", totals_by_category(transactions, "income"))
    print_totals("Expenses by category:", totals_by_category(transactions, "expense"))
    print(f"\nTotal income:   {format_money(total(transactions, 'income'))}")
    print(f"Total expenses: {format_money(total(transactions, 'expense'))}")
    print(f"Balance:        {format_money(balance(transactions))}")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expense")
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            delete_transaction()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")