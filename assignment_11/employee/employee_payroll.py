from employee import Employee
from hourly_employee import HourlyEmployee
from salary_employee import SalaryEmployee
from commission_employee import CommissionEmployee


def main():
    departments = {
        "Sales": [
            HourlyEmployee("Nick DeFalco", 52000.00),
            SalaryEmployee("Applejack Johnson", 44000.00),
            SalaryEmployee("Mario Dubois", 77200.00, "Salaried Employee")
        ],
        "Engineering": [
            SalaryEmployee("Anthony Jo", 98000.00),
            Employee("Stephanie Johnson", 31200.00)
        ],
        "Maintenance": [
            CommissionEmployee("Dominic Togo", 20000.00, 45000.00),
            HourlyEmployee("Christina Gonzalez", 41184.00)
        ],
        "HR": [
            HourlyEmployee("Geoffrey Day", 135200.00)
        ]
    }

    for department, employees in departments.items():
        print(f"Department: {department}")
        total_payroll = 0.0

        for employee in employees:
            pay = employee.get_pay()
            total_payroll += pay
            print(
                f"    {employee.name} ({employee.employee_type}): "
                f"${pay:.2f}"
            )

            if isinstance(employee, CommissionEmployee):
                print(f"        {employee.get_commission_breakdown()}")

        print(f"Total Payroll: ${total_payroll:.2f}\n")


if __name__ == "__main__":
    main()
