from patient import Patient
from procedure import Procedure


def main():
    print("Enter the patient's information:")
    first_name = input("First Name: ")
    middle_name = input("Middle Name: ")
    last_name = input("Last Name: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("ZIP: ")
    phone = input("Phone: ")
    emergency_contact = input("Emergency Contact: ")
    emergency_phone = input("Emergency Phone: ")

    patient = Patient(
        first_name, middle_name, last_name, address, city, state,
        zip_code, phone, emergency_contact, emergency_phone
    )

    procedures = []
    number_of_procedures = int(
        input("How many procedures would you like to enter? ")
    )

    for number in range(1, number_of_procedures + 1):
        print(f"\nEnter information for procedure {number}:")
        name = input("Procedure: ")
        date = input("Date: ")
        practitioner = input("Practitioner: ")
        charge = float(input("Charge: "))

        procedures.append(Procedure(name, date, practitioner, charge))

    print("\n" + str(patient))

    for procedure in procedures:
        print()
        print(procedure)


if __name__ == "__main__":
    main()
