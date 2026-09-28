import json
import os


FILE_NAME = "accounts.json"


class BankAccount:

    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be greater than 0.")
            return False

        self.balance += amount
        print(f"✅ ₹{amount:.2f} deposited successfully.")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be greater than 0.")
            return False

        if amount > self.balance:
            print("❌ Insufficient balance.")
            return False

        self.balance -= amount
        print(f"✅ ₹{amount:.2f} withdrawn successfully.")
        return True

    def display_account(self):
        print("\n----- Account Details -----")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print("---------------------------")

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }


def load_accounts():
    accounts = {}

    if not os.path.exists(FILE_NAME):
        return accounts

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for account_number, details in data.items():
            accounts[account_number] = BankAccount(
                details["account_number"],
                details["name"],
                details["balance"]
            )

    except (json.JSONDecodeError, KeyError):
        print("⚠️ Account file could not be read.")

    return accounts


def save_accounts(accounts):
    data = {}

    for account_number, account in accounts.items():
        data[account_number] = account.to_dict()

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def create_account(accounts):

    print("\n----- Create Account -----")

    account_number = input("Enter account number: ").strip()

    if not account_number:
        print("❌ Account number cannot be empty.")
        return

    if account_number in accounts:
        print("❌ Account already exists.")
        return

    name = input("Enter account holder name: ").strip()

    if not name:
        print("❌ Name cannot be empty.")
        return

    accounts[account_number] = BankAccount(
        account_number,
        name
    )

    save_accounts(accounts)

    print("✅ Account created successfully.")


def deposit_money(accounts):

    print("\n----- Deposit Money -----")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("❌ Account not found.")
        return

    try:
        amount = float(input("Enter deposit amount: "))

        if accounts[account_number].deposit(amount):
            save_accounts(accounts)

    except ValueError:
        print("❌ Please enter a valid number.")


def withdraw_money(accounts):

    print("\n----- Withdraw Money -----")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("❌ Account not found.")
        return

    try:
        amount = float(input("Enter withdrawal amount: "))

        if accounts[account_number].withdraw(amount):
            save_accounts(accounts)

    except ValueError:
        print("❌ Please enter a valid number.")


def check_balance(accounts):

    print("\n----- Check Balance -----")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("❌ Account not found.")
        return

    print(
        f"Current Balance: "
        f"₹{accounts[account_number].balance:.2f}"
    )


def search_account(accounts):

    print("\n----- Search Account -----")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("❌ Account not found.")
        return

    accounts[account_number].display_account()


def display_all_accounts(accounts):

    print("\n----- All Accounts -----")

    if not accounts:
        print("No accounts available.")
        return

    for account in accounts.values():
        account.display_account()


def delete_account(accounts):

    print("\n----- Delete Account -----")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("❌ Account not found.")
        return

    confirm = input(
        "Are you sure you want to delete this account? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        del accounts[account_number]
        save_accounts(accounts)
        print("✅ Account deleted successfully.")
    else:
        print("❌ Delete operation cancelled.")


def main():

    accounts = load_accounts()

    print("===================================")
    print("     BANK ACCOUNT MANAGEMENT")
    print("===================================")

    while True:

        print("\n========== MENU ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Account Details")
        print("6. Search Account")
        print("7. Display All Accounts")
        print("8. Delete Account")
        print("9. Exit")
        print("==========================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            deposit_money(accounts)

        elif choice == "3":
            withdraw_money(accounts)

        elif choice == "4":
            check_balance(accounts)

        elif choice == "5":
            account_number = input(
                "Enter account number: "
            ).strip()

            if account_number in accounts:
                accounts[account_number].display_account()
            else:
                print("❌ Account not found.")

        elif choice == "6":
            search_account(accounts)

        elif choice == "7":
            display_all_accounts(accounts)

        elif choice == "8":
            delete_account(accounts)

        elif choice == "9":
            save_accounts(accounts)
            print("\n✅ Data saved successfully.")
            print("Thank you for using Bank Account Management.")
            break

        else:
            print("❌ Invalid choice. Please select 1-9.")


if __name__ == "__main__":
    main()