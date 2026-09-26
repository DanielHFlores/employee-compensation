from hourly_employee import HourlyEmployee


class HourlyEmployeeWithCommission(HourlyEmployee):
    def __init__(
        self,
        name,
        employee_id,
        hourly_rate,
        hours_worked,
        commission
    ):
        super().__init__(name, employee_id, hourly_rate, hours_worked)
        self.commission = commission

    def compute_pay(self):
        return super().compute_pay() + self.commission