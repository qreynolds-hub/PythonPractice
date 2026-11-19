from employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, base_pay, commission):
        super().__init__(name, base_pay + commission, "Commission Employee")
        self.base_pay = base_pay
        self.commission = commission

    def get_pay(self):
        return self.base_pay + self.commission

    def get_commission_breakdown(self):
        percentage = self.commission / self.get_pay() * 100
        return (
            f"Base ${self.base_pay:.2f} + Commission ${self.commission:.2f} "
            f"({percentage:.1f}% of earnings)"
        )
