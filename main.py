from model import Transaction
from validation import get_amount, get_category

transactions = []


def format_money(cents):
    return f"{cents // 100:,}.{cents % 100:02d}"


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


def view_transactions():
    print("\n--- All transactions ---")
    if not transactions:
        print("No transactions yet.")
        return

    for number, t in enumerate(transactions, start=1):
        sign = "+" if t.type == "income" else "-"
        print(f"{number}. {sign}{format_money(t.amount)}  {t.category}  {t.note}")


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
            print("View summary: coming soon")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()