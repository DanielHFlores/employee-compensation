from contract import Contract


class HourlyContract(Contract):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_payment(self):
        return self.hourly_rate * self.hours_worked