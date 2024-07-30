class Company():
    def __init__(self, name):
        self.company_name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def remove_department(self, department):
        self.departments = [dept for dept in self.departments if dept.name != department]

    def list_departments(self):
        print(f"Company: {self.company_name}")
        for dept in self.departments:
            dept.list_employees()