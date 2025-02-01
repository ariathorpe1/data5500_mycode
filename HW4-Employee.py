# "How can I write a method to increase an employee's salary by a percentage?"
# "What's the correct way to modify an object's attribute in Python?"



class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

emp = Employee("John", 5000)
emp.increase_salary(10)
print("Updated Salary:", emp.salary)
