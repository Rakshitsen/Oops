from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass  # Abstract method (must be implemented in child classes)

    def employee_info(self):
        print("Employee is a class that has a method to calculate salary.")

class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_salary(self):
        print(f"Salary of {self.name} is {self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        print(f"Salary of {self.name} is {self.hourly_wage * self.hours_worked}")

# Creating objects and calling the abstract method
f1 = FullTimeEmployee("Rakshit", 50000)
f1.calculate_salary()  # Output: Salary of Rakshit is 50000

p1 = PartTimeEmployee("Rahul", 100, 40)
p1.calculate_salary()  # Output: Salary of Rahul is 4000

