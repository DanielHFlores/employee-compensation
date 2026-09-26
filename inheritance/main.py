from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee
from freelancer import Freelancer
from hourly_employee_with_commission import HourlyEmployeeWithCommission
from salaried_employee_with_commission import SalariedEmployeeWithCommission
from freelancer_with_commission import FreelancerWithCommission


employees = [
    HourlyEmployee("Ana", 1, 100, 40),
    SalariedEmployee("Luis", 2, 15000),
    Freelancer("Carlos", 3, 3000, 2),

    HourlyEmployeeWithCommission("Maria", 4, 100, 40, 500),
    SalariedEmployeeWithCommission("Pedro", 5, 15000, 1000),
    FreelancerWithCommission("Sofia", 6, 3000, 2, 750)
]

for employee in employees:
    print(
        f"{employee.name} ({employee.__class__.__name__}): "
        f"${employee.compute_pay():.2f}"
    )