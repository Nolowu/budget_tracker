#from model import Transaction

#t = Transaction("expense", "food", 1500, "lunch")

#t = Transaction("expense", "food", 1500)
#print(t)
#from model import Transaction

#t = Transaction("expense", "food", 1500, "lunch")
#t2 = Transaction("income", "allowance", 50000)
#print(t)
#print(t2)
#print(t.amount)
from model import Transaction

transactions = []


def show_menu():
    print("\n=== Student Budget Tracker ===")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all transactions")
    print("4. View summary")
    print("5. Quit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            print("Add income: coming soon")
        elif choice == "2":
            print("Add expense: coming soon")
        elif choice == "3":
            print("View transactions: coming soon")
        elif choice == "4":
            print("View summary: coming soon")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()