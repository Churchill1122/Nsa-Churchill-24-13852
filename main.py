from expense_manager import create_expense, calculate_total_expenses
from file_handler import save_expense, load_expenses

def main():
    print("=== Expense Tracker ===")

    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")

            expense = create_expense(amount, category, description)
            expenses.append(expense)
            save_expense(expense)

            print("Expense added successfully.")

        elif choice == "2":
            print("\n--- Expenses ---")
            for expense in expenses:
                print(
                    f"{expense['category']} - {expense['description']} : ₦{expense['amount']}"
                )

        elif choice == "3":
            total = calculate_total_expenses(expenses)
            print(f"\nTotal Expenses: ₦{total}")

        elif choice == "4":
            print("Exiting Expense Tracker...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
