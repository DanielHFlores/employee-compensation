class Employee:
    def __init__(self, name, employee_id, contract, commission=None):
        self.name = name
        self.employee_id = employee_id
        self.contract = contract
        self.commission = commission

    def compute_pay(self):
        pay = self.contract.get_payment()

        if self.commission is not None:
            pay += self.commission.get_payment()

        return pay