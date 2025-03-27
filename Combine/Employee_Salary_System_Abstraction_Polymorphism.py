from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass  # Abstract method

    def employee_info(self):
        print("Employee class manages salary calculations.")

class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        print(f"Salary of {self.name} (Full-Time) is {self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calculate_salary(self):
        salary = self.hourly_wage * self.hours_worked
        print(f"Salary of {self.name} (Part-Time) is {salary}")

# Creating Employee objects
f1 = FullTimeEmployee("Rakshit", 50000)
p1 = PartTimeEmployee("Rahul", 100, 40)

f1.calculate_salary()  # Output: Full-Time salary
p1.calculate_salary()  # Output: Part-Time salary

