import json
from datetime import datetime


DATA_FILE = "bills.json"


class GroceryBill:
    def __init__(self, bill_id, customer_name, items):
        self.bill_id = bill_id
        self.customer_name = customer_name
        self.items = items
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item["quantity"] * item["price"]

        return total

    def display_bill(self):
        print("\n========== GROCERY BILL ==========")
        print("Bill ID      :", self.bill_id)
        print("Customer     :", self.customer_name)
        print("Date         :", self.date)
        print("----------------------------------")

        for item in self.items:
            amount = item["quantity"] * item["price"]

            print(
                f'{item["name"]} | '
                f'Qty: {item["quantity"]} | '
                f'Price: ₹{item["price"]:.2f} | '
                f'Amount: ₹{amount:.2f}'
            )

        print("----------------------------------")
        print(f"Total Amount : ₹{self.calculate_total():.2f}")
        print("==================================")


def load_bills():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_bills(bills):
    with open(DATA_FILE, "w") as file:
        json.dump(bills, file, indent=4)


def create_bill():
    bills = load_bills()

    bill_id = input("Enter Bill ID: ")
    customer_name = input("Enter Customer Name: ")

    items = []

    while True:
        name = input("\nEnter Item Name: ")

        try:
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
        except ValueError:
            print("Invalid quantity or price.")
            continue

        item = {
            "name": name,
            "quantity": quantity,
            "price": price
        }

        items.append(item)

        more = input("Add another item? (yes/no): ").lower()

        if more != "yes":
            break

    bill = GroceryBill(
        bill_id,
        customer_name,
        items
    )

    bills.append({
        "bill_id": bill.bill_id,
        "customer_name": bill.customer_name,
        "items": bill.items,
        "date": bill.date,
        "total": bill.calculate_total()
    })

    save_bills(bills)

    bill.display_bill()

    print("\nBill saved successfully!")


def view_all_bills():
    bills = load_bills()

    if not bills:
        print("\nNo bills found.")
        return

    print("\n========== ALL BILLS ==========")

    for bill in bills:
        print(
            f'Bill ID: {bill["bill_id"]} | '
            f'Customer: {bill["customer_name"]} | '
            f'Total: ₹{bill["total"]:.2f}'
        )


def search_bill():
    bills = load_bills()

    bill_id = input("Enter Bill ID to search: ")

    for data in bills:
        if data["bill_id"] == bill_id:

            bill = GroceryBill(
                data["bill_id"],
                data["customer_name"],
                data["items"]
            )

            bill.date = data["date"]
            bill.display_bill()

            return

    print("Bill not found.")


def delete_bill():
    bills = load_bills()

    bill_id = input("Enter Bill ID to delete: ")

    new_bills = [
        bill for bill in bills
        if bill["bill_id"] != bill_id
    ]

    if len(new_bills) == len(bills):
        print("Bill not found.")
    else:
        save_bills(new_bills)
        print("Bill deleted successfully.")


def main():

    while True:

        print("\n====== GROCERY BILLING SYSTEM ======")
        print("1. Create Bill")
        print("2. View All Bills")
        print("3. Search Bill")
        print("4. Delete Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_bill()

        elif choice == "2":
            view_all_bills()

        elif choice == "3":
            search_bill()

        elif choice == "4":
            delete_bill()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()