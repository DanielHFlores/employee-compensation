from contract import Contract


class FreelancerContract(Contract):
    def __init__(self, project_rate, projects_completed):
        self.project_rate = project_rate
        self.projects_completed = projects_completed

    def get_payment(self):
        return self.project_rate * self.projects_completed