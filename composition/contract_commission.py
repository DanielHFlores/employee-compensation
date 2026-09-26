from commission import Commission


class ContractCommission(Commission):
    def __init__(self, commission):
        self.commission = commission

    def get_payment(self):
        return self.commission