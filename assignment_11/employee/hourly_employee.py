from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, annual_pay):
        super().__init__(name, annual_pay, "Hourly Employee")

    def get_pay(self):
        return self.annual_pay
