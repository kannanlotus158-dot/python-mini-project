import json
import os

FILE_NAME = "students.json"


class Student:
    def __init__(self, roll_number, name, marks):
        self.roll_number = roll_number
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks.values())

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def result(self):
        if any(mark < 35 for mark in self.marks.values()):
            return "FAIL"
        return "PASS"

    def display(self):
        print("\n----- Student Result -----")
        print(f"Roll Number : {self.roll_number}")
        print(f"Name        : {self.name}")

        for subject, mark in self.marks.items():
            print(f"{subject:<12}: {mark}")

        print(f"Total       : {self.total()}")
        print(f"Average     : {self.average():.2f}")
        print(f"Grade       : {self.grade()}")
        print(f"Result      : {self.result()}")
        print("--------------------------")

    def to_dict(self):
        return {
            "roll_number": self.roll_number,
            "name": self.name,
            "marks": self.marks
        }


def load_students():
    students = {}

    if not os.path.exists(FILE_NAME):
        return students

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for roll_number, details in data.items():
            students[roll_number] = Student(
                details["roll_number"],
                details["name"],
                details["marks"]
            )

    except (json.JSONDecodeError, KeyError):
        print("Error reading student data.")

    return students


def save_students(students):
    data = {}

    for roll_number, student in students.items():
        data[roll_number] = student.to_dict()

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter {subject} mark: "))

            if 0 <= mark <= 100:
                return mark

            print("Mark must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    print("\n----- Add Student -----")

    roll_number = input("Enter roll number: ").strip()

    if not roll_number:
        print("Roll number cannot be empty.")
        return

    if roll_number in students:
        print("Student already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    subjects = ["Python", "HTML", "CSS", "JavaScript"]

    marks = {}

    for subject in subjects:
        marks[subject] = get_mark(subject)

    students[roll_number] = Student(
        roll_number,
        name,
        marks
    )

    save_students(students)

    print("Student added successfully.")


def view_student(students):
    roll_number = input("Enter roll number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    students[roll_number].display()


def view_all_students(students):
    if not students:
        print("No students available.")
        return

    for student in students.values():
        student.display()


def search_student(students):
    roll_number = input("Enter roll number: ").strip()

    if roll_number in students:
        student = students[roll_number]

        print("\nStudent Found")
        print(f"Roll Number: {student.roll_number}")
        print(f"Name: {student.name}")
    else:
        print("Student not found.")


def update_marks(students):
    roll_number = input("Enter roll number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]

    print(f"\nUpdating marks for {student.name}")

    for subject in student.marks:
        student.marks[subject] = get_mark(subject)

    save_students(students)

    print("Marks updated successfully.")


def delete_student(students):
    roll_number = input("Enter roll number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    confirm = input(
        "Are you sure you want to delete? (yes/no): "
    ).lower()

    if confirm == "yes":
        del students[roll_number]
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Delete cancelled.")


def main():
    students = load_students()

    print("====================================")
    print("     STUDENT RESULT MANAGEMENT")
    print("====================================")

    while True:

        print("\n========== MENU ==========")
        print("1. Add Student")
        print("2. View Student Result")
        print("3. View All Students")
        print("4. Search Student")
        print("5. Update Marks")
        print("6. Delete Student")
        print("7. Exit")
        print("==========================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_student(students)

        elif choice == "3":
            view_all_students(students)

        elif choice == "4":
            search_student(students)

        elif choice == "5":
            update_marks(students)

        elif choice == "6":
            delete_student(students)

        elif choice == "7":
            save_students(students)
            print("Data saved successfully.")
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()