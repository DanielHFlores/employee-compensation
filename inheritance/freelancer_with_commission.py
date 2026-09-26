from freelancer import Freelancer


class FreelancerWithCommission(Freelancer):
    def __init__(
        self,
        name,
        employee_id,
        project_rate,
        projects_completed,
        commission
    ):
        super().__init__(
            name,
            employee_id,
            project_rate,
            projects_completed
        )
        self.commission = commission

    def compute_pay(self):
        return super().compute_pay() + self.commission