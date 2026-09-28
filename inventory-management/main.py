import json

DATA_FILE = "inventory.json"


def load_inventory():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_inventory(inventory):
    with open(DATA_FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def add_product():
    inventory = load_inventory()

    product_id = input("Enter Product ID: ").strip()
    name = input("Enter Product Name: ").strip()

    if product_id == "" or name == "":
        print("Product ID and Name cannot be empty.")
        return

    try:
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return

    for product in inventory:
        if product["product_id"] == product_id:
            print("Product ID already exists.")
            return

    product = {
        "product_id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    save_inventory(inventory)

    print("Product added successfully!")


def view_products():
    inventory = load_inventory()

    if len(inventory) == 0:
        print("No products found.")
        return

    print("\n========== INVENTORY ==========")

    for product in inventory:
        print("Product ID :", product["product_id"])
        print("Name       :", product["name"])
        print("Price      :", product["price"])
        print("Quantity   :", product["quantity"])
        print("------------------------------")


def search_product():
    inventory = load_inventory()

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["product_id"] == product_id:
            print("\nProduct Found")
            print("Product ID :", product["product_id"])
            print("Name       :", product["name"])
            print("Price      :", product["price"])
            print("Quantity   :", product["quantity"])
            return

    print("Product not found.")


def update_product():
    inventory = load_inventory()

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["product_id"] == product_id:

            new_name = input("Enter New Name: ").strip()

            try:
                new_price = float(input("Enter New Price: "))
                new_quantity = int(input("Enter New Quantity: "))
            except ValueError:
                print("Please enter valid numbers.")
                return

            if new_price < 0 or new_quantity < 0:
                print("Price and quantity cannot be negative.")
                return

            product["name"] = new_name
            product["price"] = new_price
            product["quantity"] = new_quantity

            save_inventory(inventory)

            print("Product updated successfully!")
            return

    print("Product not found.")


def sell_product():
    inventory = load_inventory()

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["product_id"] == product_id:

            try:
                quantity = int(input("Enter Quantity to Sell: "))
            except ValueError:
                print("Please enter a valid quantity.")
                return

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                return

            if quantity > product["quantity"]:
                print("Not enough stock.")
                return

            product["quantity"] -= quantity

            total = quantity * product["price"]

            save_inventory(inventory)

            print("Sale completed successfully!")
            print("Total Amount:", total)
            print("Remaining Stock:", product["quantity"])
            return

    print("Product not found.")


def delete_product():
    inventory = load_inventory()

    product_id = input("Enter Product ID: ").strip()

    for product in inventory:
        if product["product_id"] == product_id:

            inventory.remove(product)
            save_inventory(inventory)

            print("Product deleted successfully!")
            return

    print("Product not found.")


def main():
    while True:

        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Sell Product")
        print("6. Delete Product")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            sell_product()

        elif choice == "6":
            delete_product()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()