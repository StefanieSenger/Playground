class Person():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Allow the caller to retrieve the salary
    def getSalary(self):
        return self.salary

    # Allow the caller to set a new salary
    def setSalary(self, salary):
        self.salary = salary

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

# Get the values of the salary variable directly
print(oPerson1.salary)
print(oPerson2.salary)

# Change the salary variable directly
oPerson1.salary = 100000
oPerson2.salary = 111111

# Get the updated salaries and print again
print(oPerson1.salary)
print(oPerson2.salary)

# Using getter and setter methods
print(oPerson1.getSalary())
oPerson1.setSalary(0) # fired
print(oPerson1.getSalary())
