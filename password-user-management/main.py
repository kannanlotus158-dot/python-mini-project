import json
import hashlib

DATA_FILE = "users.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file, indent=4)


def register_user():
    users = load_users()

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ")

    if username == "":
        print("Username cannot be empty.")
        return

    if len(password) < 6:
        print("Password must contain at least 6 characters.")
        return

    for user in users:
        if user["username"] == username:
            print("Username already exists.")
            return

    new_user = {
        "username": username,
        "password": hash_password(password)
    }

    users.append(new_user)
    save_users(users)

    print("User registered successfully!")


def login_user():
    users = load_users()

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ")

    password_hash = hash_password(password)

    for user in users:
        if (
            user["username"] == username
            and user["password"] == password_hash
        ):
            print("Login successful!")
            print("Welcome,", username)
            return

    print("Invalid username or password.")


def view_users():
    users = load_users()

    if len(users) == 0:
        print("No users found.")
        return

    print("\n========== USERS ==========")

    for user in users:
        print("Username:", user["username"])


def change_password():
    users = load_users()

    username = input("Enter Username: ").strip()
    old_password = input("Enter Current Password: ")

    old_password_hash = hash_password(old_password)

    for user in users:
        if (
            user["username"] == username
            and user["password"] == old_password_hash
        ):
            new_password = input("Enter New Password: ")

            if len(new_password) < 6:
                print("Password must contain at least 6 characters.")
                return

            user["password"] = hash_password(new_password)
            save_users(users)

            print("Password changed successfully!")
            return

    print("Invalid username or current password.")


def delete_user():
    users = load_users()

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ")

    password_hash = hash_password(password)

    for user in users:
        if (
            user["username"] == username
            and user["password"] == password_hash
        ):
            users.remove(user)
            save_users(users)

            print("User deleted successfully!")
            return

    print("Invalid username or password.")


def main():
    while True:

        print("\n====== PASSWORD & USER MANAGEMENT ======")
        print("1. Register User")
        print("2. Login")
        print("3. View Users")
        print("4. Change Password")
        print("5. Delete User")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()

        elif choice == "2":
            login_user()

        elif choice == "3":
            view_users()

        elif choice == "4":
            change_password()

        elif choice == "5":
            delete_user()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()