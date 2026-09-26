from contract import Contract


class SalariedContract(Contract):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def get_payment(self):
        return self.monthly_salary