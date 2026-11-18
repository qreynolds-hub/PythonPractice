
import pickle
import os
from employee import Employee

# File used to store employee information.
FILENAME = "employee.dat"


# --- Load employee records -----------------------------------------
def load_employees():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "rb") as file:
                return pickle.load(file)
        except (EOFError, pickle.UnpicklingError):
            return {}
    return {}


# --- Save employee records -----------------------------------------
def save_employees(employees):
    with open(FILENAME, "wb") as file:
        pickle.dump(employees, file)


# --- Display menu --------------------------------------------------
def display_menu():
    print("\nMenu")
    print("------------------------------------------")
    print("1. Look up an employee")
    print("2. Add a new employee")
    print("3. Change an existing employee")
    print("4. Delete an employee")
    print("5. Quit the program")


# --- Look up an employee -------------------------------------------
def look_up_employee(employees):
    employee_id = input("Enter an employee ID number: ")

    if employee_id in employees:
        print(employees[employee_id])
    else:
        print("The specified ID number was not found")


# --- Add a new employee --------------------------------------------
def add_employee(employees):
    name = input("Enter employee name: ")
    employee_id = input("Enter employee ID number: ")

    if employee_id in employees:
        print("An employee with that ID number already exists.")
        return

    department = input("Enter employee department: ")
    title = input("Enter employee title: ")

    employee = Employee(name, employee_id, department, title)

    employees[employee_id] = employee
    save_employees(employees)

    print("The new employee has been added.")


# --- Change an existing employee -----------------------------------
def change_employee(employees):
    employee_id = input("Enter employee ID number: ")

    if employee_id in employees:
        employee = employees[employee_id]

        name = input("Enter the new name: ")
        department = input("Enter the new department: ")
        title = input("Enter the new title: ")

        employee.set_name(name)
        employee.set_department(department)
        employee.set_title(title)

        save_employees(employees)

        print("Employee information updated.")
    else:
        print("The specified ID number was not found")


# --- Delete an employee --------------------------------------------
def delete_employee(employees):
    employee_id = input("Enter employee ID number: ")

    if employee_id in employees:
        del employees[employee_id]
        save_employees(employees)

        print("Employee information deleted.")
    else:
        print("The specified ID number was not found")


# --- Main program --------------------------------------------------
def main():
    employees = load_employees()

    choice = 0

    while choice != 5:
        display_menu()

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a valid menu choice.")
            continue

        if choice == 1:
            look_up_employee(employees)

        elif choice == 2:
            add_employee(employees)

        elif choice == 3:
            change_employee(employees)

        elif choice == 4:
            delete_employee(employees)

        elif choice == 5:
            print("Program ended.")

        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
