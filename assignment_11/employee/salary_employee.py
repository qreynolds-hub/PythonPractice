from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, annual_pay, employee_type="Salary Employee"):
        super().__init__(name, annual_pay, employee_type)

    def get_pay(self):
        return self.annual_pay
