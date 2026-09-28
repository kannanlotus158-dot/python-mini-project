import json

DATA_FILE = "books.json"


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }


def load_books():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_books(books):
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    for book in books:
        if book["book_id"] == book_id:
            print("Book ID already exists.")
            return

    book = Book(book_id, title, author)

    books.append(book.to_dict())
    save_books(books)

    print("Book added successfully!")


def view_books():
    books = load_books()

    if not books:
        print("No books found.")
        return

    print("\n========== BOOK LIST ==========")

    for book in books:
        status = "Available" if book["available"] else "Issued"

        print("Book ID :", book["book_id"])
        print("Title   :", book["title"])
        print("Author  :", book["author"])
        print("Status  :", status)
        print("-------------------------------")


def search_book():
    books = load_books()

    book_id = input("Enter Book ID to search: ")

    for book in books:
        if book["book_id"] == book_id:

            print("\n========== BOOK DETAILS ==========")
            print("Book ID :", book["book_id"])
            print("Title   :", book["title"])
            print("Author  :", book["author"])

            status = "Available" if book["available"] else "Issued"
            print("Status  :", status)

            return

    print("Book not found.")


def issue_book():
    books = load_books()

    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["book_id"] == book_id:

            if not book["available"]:
                print("Book is already issued.")
                return

            book["available"] = False
            save_books(books)

            print("Book issued successfully!")
            return

    print("Book not found.")


def return_book():
    books = load_books()

    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["book_id"] == book_id:

            if book["available"]:
                print("Book is already available.")
                return

            book["available"] = True
            save_books(books)

            print("Book returned successfully!")
            return

    print("Book not found.")


def delete_book():
    books = load_books()

    book_id = input("Enter Book ID to delete: ")

    for book in books:
        if book["book_id"] == book_id:

            books.remove(book)
            save_books(books)

            print("Book deleted successfully!")
            return

    print("Book not found.")


def main():

    while True:

        print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            issue_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()