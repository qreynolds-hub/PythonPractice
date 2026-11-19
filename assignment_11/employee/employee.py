class Employee:
    """Base class for employees."""

    def __init__(self, name, annual_pay, employee_type="Employee"):
        self.name = name
        self.annual_pay = annual_pay
        self.employee_type = employee_type

    def get_pay(self):
        return self.annual_pay
