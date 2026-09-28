import json

DATA_FILE = "patients.json"


class Patient:
    def __init__(self, patient_id, name, age, disease, phone):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.phone = phone

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
            "phone": self.phone
        }


def load_patients():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_patients(patients):
    with open(DATA_FILE, "w") as file:
        json.dump(patients, file, indent=4)


def add_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")

    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age.")
        return

    disease = input("Enter Disease: ")
    phone = input("Enter Phone: ")

    patient = Patient(
        patient_id,
        name,
        age,
        disease,
        phone
    )

    patients.append(patient.to_dict())
    save_patients(patients)

    print("Patient added successfully!")


def view_patients():
    patients = load_patients()

    if not patients:
        print("No patients found.")
        return

    print("\n========== PATIENT LIST ==========")

    for patient in patients:
        print("Patient ID :", patient["patient_id"])
        print("Name       :", patient["name"])
        print("Age        :", patient["age"])
        print("Disease    :", patient["disease"])
        print("Phone      :", patient["phone"])
        print("----------------------------------")


def search_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID to search: ")

    for patient in patients:
        if patient["patient_id"] == patient_id:
            print("\nPatient Found!")
            print("Patient ID :", patient["patient_id"])
            print("Name       :", patient["name"])
            print("Age        :", patient["age"])
            print("Disease    :", patient["disease"])
            print("Phone      :", patient["phone"])
            return

    print("Patient not found.")


def update_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID to update: ")

    for patient in patients:
        if patient["patient_id"] == patient_id:

            patient["name"] = input("Enter new name: ")

            try:
                patient["age"] = int(input("Enter new age: "))
            except ValueError:
                print("Invalid age.")
                return

            patient["disease"] = input("Enter new disease: ")
            patient["phone"] = input("Enter new phone: ")

            save_patients(patients)

            print("Patient updated successfully!")
            return

    print("Patient not found.")


def delete_patient():
    patients = load_patients()

    patient_id = input("Enter Patient ID to delete: ")

    new_patients = [
        patient
        for patient in patients
        if patient["patient_id"] != patient_id
    ]

    if len(new_patients) == len(patients):
        print("Patient not found.")
    else:
        save_patients(new_patients)
        print("Patient deleted successfully.")


def main():

    while True:

        print("\n====== HOSPITAL PATIENT MANAGEMENT ======")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()