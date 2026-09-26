from employee import Employee


class Freelancer(Employee):
    def __init__(self, name, employee_id, project_rate, projects_completed):
        super().__init__(name, employee_id)
        self.project_rate = project_rate
        self.projects_completed = projects_completed

    def compute_pay(self):
        return self.project_rate * self.projects_completed