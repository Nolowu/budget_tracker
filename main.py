from model import Transaction
from validation import get_amount, get_category
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
    print("5. Quit")


def add_transaction(kind):
    print(f"\n--- Add {kind} ---")
    category = get_category("Category (e.g. food, rent, salary): ")
    amount = get_amount("Amount: ")
    note = input("Note (optional): ").strip()

    transactions.append(Transaction(kind, category, amount, note))
    print(f"Saved: {kind} of {format_money(amount)} in '{category}'.")

    try:
        save_transactions(transactions)
    except OSError:
        print("Warning: could not write to the data file.")


def view_transactions():
    print("\n--- All transactions ---")
    if not transactions:
        print("No transactions yet.")
        return

    for number, t in enumerate(transactions, start=1):
        sign = "+" if t.type == "income" else "-"
        print(f"{number}. {sign}{format_money(t.amount)}  {t.category}  {t.note}")


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
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_transaction("income")
        elif choice == "2":
            add_transaction("expense")
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")