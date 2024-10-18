from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_salary, overtime_rate):
        self.name = name
        self.base_salary = base_salary
        self.overtime_rate = overtime_rate

    @abstractmethod
    def calculate_salary(self, hours_worked):
        pass

    def __str__(self):
        return f"{self.name}: Total Salary - {self.calculate_salary()} kyats"

class PermanentEmployee(Employee):
    def __init__(self, name, base_salary, bonus_rate, overtime_rate):
        super().__init__(name, base_salary, overtime_rate)
        self.bonus_rate = bonus_rate

    def calculate_salary(self, hours_worked=160):
        total_salary = self.base_salary + (self.base_salary * self.bonus_rate)
        return total_salary

class HourlyEmployee(Employee):
    def calculate_salary(self, hours_worked):
        total_salary = self.base_salary * hours_worked + (self.overtime_rate * hours_worked)
        return total_salary

BASE_SALARIES = {
    "Senior Manager": 1000000,
    "Manager": 800000,
    "Cleaning Staff": 300000,
    "Sales Person": 5000000
}

BONUS_RATES = {
    "Senior Manager": 0.1,
    "Manager": 0.1,
    "Sales Person": 0.1,
    "Cleaning Staff": 0.07
}

HOURLY_BASE_SALARY = 2500
OVERTIME_RATE = 5000

senior_manager = PermanentEmployee("John Doe", BASE_SALARIES["Senior Manager"], BONUS_RATES["Senior Manager"], OVERTIME_RATE)
manager = PermanentEmployee("Jane Smith", BASE_SALARIES["Manager"], BONUS_RATES["Manager"], OVERTIME_RATE)
cleaning_staff = PermanentEmployee("Alice Brown", BASE_SALARIES["Cleaning Staff"], BONUS_RATES["Cleaning Staff"], OVERTIME_RATE)
sales_person = PermanentEmployee("Bob Johnson", BASE_SALARIES["Sales Person"], BONUS_RATES["Sales Person"], OVERTIME_RATE)
hourly_employee = HourlyEmployee("Sam Green", HOURLY_BASE_SALARY, OVERTIME_RATE)

print(senior_manager)
print(manager)
print(cleaning_staff)
print(sales_person)
print(hourly_employee)
