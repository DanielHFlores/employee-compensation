from salaried_employee import SalariedEmployee


class SalariedEmployeeWithCommission(SalariedEmployee):
    def __init__(
        self,
        name,
        employee_id,
        monthly_salary,
        commission
    ):
        super().__init__(name, employee_id, monthly_salary)
        self.commission = commission

    def compute_pay(self):
        return super().compute_pay() + self.commission