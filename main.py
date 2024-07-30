from employee import Employee
from department import Department
from company import Company

company = Company("RK company")

hr_department = Department("HR")
it_department = Department("IT")

company.add_department(hr_department)
company.add_department(it_department)

employee1 = Employee(1, "Kajal", "Software Engineer",400000, "Chennai")
employee2 = Employee(2, "Suraj", "Devops Engineer", 100000, "Delhi")
employee3 = Employee(3, "Hari", "Manager", 600000, "Ghaziabad")
employee4 = Employee(4, "Madhu", "HR", 1000000, "Gurgaon")
employee5 = Employee(5, "Puja", "Admin", 800000, "Pune")

it_department.add_employee(employee1)
it_department.add_employee(employee2)
it_department.add_employee(employee3)
hr_department.add_employee(employee4)
hr_department.add_employee(employee5)

company.list_departments()
