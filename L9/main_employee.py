from employee import Employee, Manager

emp = Employee("John", 3000)
mgr = Manager("Alice", 5000, "IT")

print(emp.get_details())
print(mgr.get_details())
