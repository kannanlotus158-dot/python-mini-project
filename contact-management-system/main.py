import json

DATA_FILE = "contacts.json"


class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }


def load_contacts():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(DATA_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    contacts = load_contacts()

    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contact = Contact(name, phone, email)

    contacts.append(contact.to_dict())
    save_contacts(contacts)

    print("Contact added successfully!")


def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("No contacts found.")
        return

    print("\n========== CONTACTS ==========")

    for contact in contacts:
        print("Name  :", contact["name"])
        print("Phone :", contact["phone"])
        print("Email :", contact["email"])
        print("------------------------------")


def search_contact():
    contacts = load_contacts()

    name = input("Enter name to search: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("\nContact Found!")
            print("Name  :", contact["name"])
            print("Phone :", contact["phone"])
            print("Email :", contact["email"])
            return

    print("Contact not found.")


def update_contact():
    contacts = load_contacts()

    name = input("Enter name to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            contact["phone"] = input("Enter new phone: ")
            contact["email"] = input("Enter new email: ")

            save_contacts(contacts)

            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    contacts = load_contacts()

    name = input("Enter name to delete: ").lower()

    new_contacts = [
        contact for contact in contacts
        if contact["name"].lower() != name
    ]

    if len(new_contacts) == len(contacts):
        print("Contact not found.")
    else:
        save_contacts(new_contacts)
        print("Contact deleted successfully.")


def main():

    while True:

        print("\n====== CONTACT MANAGEMENT SYSTEM ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()