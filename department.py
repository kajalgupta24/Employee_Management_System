class Department:
    def __init__(self, department_name):
        self.name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(f" - {emp}")