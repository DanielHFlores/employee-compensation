from employee import Employee
from hourly_contract import HourlyContract
from salaried_contract import SalariedContract
from freelancer_contract import FreelancerContract
from contract_commission import ContractCommission


employees = [
    Employee(
        "Ana",
        1,
        HourlyContract(100, 40)
    ),

    Employee(
        "Luis",
        2,
        SalariedContract(15000)
    ),

    Employee(
        "Carlos",
        3,
        FreelancerContract(3000, 2)
    ),

    Employee(
        "Maria",
        4,
        HourlyContract(100, 40),
        ContractCommission(500)
    ),

    Employee(
        "Pedro",
        5,
        SalariedContract(15000),
        ContractCommission(1000)
    ),

    Employee(
        "Sofia",
        6,
        FreelancerContract(3000, 2),
        ContractCommission(750)
    )
]

for employee in employees:
    print(
        f"{employee.name}: "
        f"${employee.compute_pay():.2f}"
    )