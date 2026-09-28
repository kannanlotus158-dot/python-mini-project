import json
from datetime import datetime

DATA_FILE = "expenses.json"


class Expense:
    def __init__(self, expense_id, category, amount, description):
        self.expense_id = expense_id
        self.category = category
        self.amount = amount
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "expense_id": self.expense_id,
            "category": self.category,
            "amount": self.amount,
            "description": self.description,
            "date": self.date
        }


def load_expenses():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    expenses = load_expenses()

    expense_id = input("Enter Expense ID: ")
    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    description = input("Enter Description: ")

    expense = Expense(
        expense_id,
        category,
        amount,
        description
    )

    expenses.append(expense.to_dict())
    save_expenses(expenses)

    print("Expense added successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n========== EXPENSE LIST ==========")

    for expense in expenses:
        print("ID          :", expense["expense_id"])
        print("Category    :", expense["category"])
        print("Amount      : ₹", f'{expense["amount"]:.2f}')
        print("Description :", expense["description"])
        print("Date        :", expense["date"])
        print("----------------------------------")


def calculate_total():
    expenses = load_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: ₹{total:.2f}")


def search_expense():
    expenses = load_expenses()

    expense_id = input("Enter Expense ID to search: ")

    for expense in expenses:
        if expense["expense_id"] == expense_id:
            print("\nExpense Found!")
            print("ID          :", expense["expense_id"])
            print("Category    :", expense["category"])
            print("Amount      : ₹", f'{expense["amount"]:.2f}')
            print("Description :", expense["description"])
            print("Date        :", expense["date"])
            return

    print("Expense not found.")


def delete_expense():
    expenses = load_expenses()

    expense_id = input("Enter Expense ID to delete: ")

    for expense in expenses:
        if expense["expense_id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)

            print("Expense deleted successfully!")
            return

    print("Expense not found.")


def main():

    while True:

        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            search_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()