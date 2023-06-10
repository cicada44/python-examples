#-----------------------------------------------------------------------------
#
# Trivial example for classes in Python3
#
#-----------------------------------------------------------------------------

# Create employee class
class Employee:
    # Make constructor for class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method for display salary
    def displaySalary(self):
        print("Salary of employee", self.name, "is", self.salary, end='\n\n')

    # Method for display name
    def displayNmae(self):
        print("Name of employee is", self.name, end='\n\n')

Emp1 = Employee('John', 100)
Emp2 = Employee('Ivan', 2500)

Emp1.displayNmae()
Emp2.displayNmae()
