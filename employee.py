class Employee:
    def __init__(self, emp_id, name, position, salary, location):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.location = location

    def change_location(self, new_location):
        self.location = new_location
        print(f"changed location to {self.location} for Emp Id: {self.emp_id}\n")

    def change_position(self, new_position):
        self.position = new_position
        print(self.position)

    def change_salary(self, new_salary):
        self.salary = new_salary
        print(self.salary)

    def __str__(self):
        return f"{self.emp_id}: {self.name}, {self.position}, {self.location}\n"
