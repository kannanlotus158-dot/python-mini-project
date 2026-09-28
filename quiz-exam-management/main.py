import json

DATA_FILE = "questions.json"


class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def to_dict(self):
        return {
            "question": self.question,
            "options": self.options,
            "answer": self.answer
        }


def load_questions():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_questions(questions):
    with open(DATA_FILE, "w") as file:
        json.dump(questions, file, indent=4)


def add_question():
    questions = load_questions()

    question = input("Enter Question: ")

    options = []

    for i in range(4):
        option = input(f"Enter Option {i + 1}: ")
        options.append(option)

    answer = input("Enter Correct Answer (1-4): ")

    if answer not in ["1", "2", "3", "4"]:
        print("Invalid answer.")
        return

    new_question = Question(
        question,
        options,
        answer
    )

    questions.append(new_question.to_dict())
    save_questions(questions)

    print("Question added successfully!")


def view_questions():
    questions = load_questions()

    if not questions:
        print("No questions found.")
        return

    print("\n========== QUESTIONS ==========")

    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}: {question['question']}")

        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        print("Correct Answer:", question["answer"])


def start_quiz():
    questions = load_questions()

    if not questions:
        print("No questions available.")
        return

    score = 0

    print("\n========== QUIZ START ==========")

    for index, question in enumerate(questions, start=1):

        print(f"\nQuestion {index}:")
        print(question["question"])

        for i, option in enumerate(question["options"], start=1):
            print(f"{i}. {option}")

        answer = input("Enter your answer (1-4): ")

        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                "Wrong! Correct answer:",
                question["answer"]
            )

    print("\n========== RESULT ==========")
    print("Total Questions :", len(questions))
    print("Correct Answers :", score)
    print("Wrong Answers   :", len(questions) - score)
    print("Score           :", f"{score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print("Percentage      :", f"{percentage:.2f}%")

    if percentage >= 50:
        print("Result          : PASS")
    else:
        print("Result          : FAIL")


def delete_question():
    questions = load_questions()

    if not questions:
        print("No questions found.")
        return

    view_questions()

    try:
        number = int(input("\nEnter Question Number to delete: "))
    except ValueError:
        print("Invalid number.")
        return

    if number < 1 or number > len(questions):
        print("Invalid question number.")
        return

    questions.pop(number - 1)
    save_questions(questions)

    print("Question deleted successfully!")


def main():

    while True:

        print("\n====== QUIZ / EXAM MANAGEMENT SYSTEM ======")
        print("1. Add Question")
        print("2. View Questions")
        print("3. Start Quiz")
        print("4. Delete Question")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_question()

        elif choice == "2":
            view_questions()

        elif choice == "3":
            start_quiz()

        elif choice == "4":
            delete_question()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()