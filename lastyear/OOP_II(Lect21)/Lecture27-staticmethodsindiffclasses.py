'''
# this class contain employee details
class Emp:
    #this is a constructor
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    #this is an instance method
    def display(self):
        print('Id=',self.id)
        print('Name=',self.name)
        print('Salary=',self.salary)
# This is another class which display employee details
class Myclass:
    #method to receive Emp class instance
    #and display emp details
    @staticmethod
    def mymethod(e):
        e.salary+=1000
        e.display()
#create Emp class instance e
e=Emp(10,'Mg Mg',15000.75)
#call static method of Myclass and pass e
Myclass.mymethod(e)
e1=Emp(11,'ko ko',14000.75)
#call static method of Myclass and pass e
Myclass.mymethod(e1)

###staticmethodbetterexample
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

   # @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")

# Using the static methods of MathUtils
result1 = MathUtils.add(5, 3)
result2 = MathUtils.subtract(10, 4)
result3 = MathUtils.multiply(6, 7)
result4 = MathUtils.divide(15, 3)
#result5 = MathUtils.subtract(25, 4)


print("Addition:", result1)     # Output: 8
print("Subtraction:", result2)  # Output: 6
print("Multiplication:", result3)  # Output: 42
print("Division:", result4)      # Output: 5.0
#print("Substraction:", result5)      # Output: 21
###another example
class MathUtils:
    # Method without @staticmethod
    def subtract_without_static(a, b):
        return a - b

    # Method with @staticmethod
    @staticmethod
    def subtract_with_static(a, b):
        return a - b

# Using the methods
result_without_static = MathUtils.subtract_without_static(10, 5)
result_with_static = MathUtils.subtract_with_static(10, 5)

print("Subtraction (without @staticmethod):", result_without_static)  # Output: 5
print("Subtraction (with @staticmethod):", result_with_static)        # Output: 5
'''
##antother temperature example
class TemperatureConverter:
    def __init__(self, temperature):
        self.temperature = temperature

    # Instance method to convert Celsius to Fahrenheit
    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    # Static method to convert Fahrenheit to Celsius
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_temp):
        return (fahrenheit_temp - 32) * 5/9

# Creating an instance of TemperatureConverter
converter = TemperatureConverter(30)

# Using the instance method to convert Celsius to Fahrenheit
celsius_temperature = converter.temperature
fahrenheit_result = converter.celsius_to_fahrenheit()

print(f"{celsius_temperature}°C in Fahrenheit:", fahrenheit_result)

# Using the static method to convert Fahrenheit to Celsius
fahrenheit_temperature = 86
celsius_result = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temperature)

print(f"{fahrenheit_temperature}°F in Celsius:", celsius_result)
