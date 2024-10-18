class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 0  # private attribute

    def get_odometer_reading(self):
        return self.__odometer_reading

    def update_odometer(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def drive(self, miles):
        self.__odometer_reading += miles


# Creating an instance of Car
my_car = Car("Toyota", "Camry", 2020)

# Accessing attributes directly (not recommended due to encapsulation)
''' In Python, attributes and methods can be accessed from outside the class,
but it's a good practice to use methods for accessing
and modifying attributes instead of directly accessing them.'''
print(my_car.make)  # Output: Toyota

# Accessing attributes via methods
print(my_car.get_odometer_reading())  # Output: 0

# Trying to update odometer directly
'''The __odometer_reading attribute is marked as private using double underscores (__).
This means it cannot be accessed or modified directly from outside the class.
Access to the __odometer_reading attribute is provided through getter and setter methods
get_odometer_reading() and update_odometer()). '''

#my_car.__odometer_reading = 1000 

# Updating odometer using the update_odometer method
my_car.update_odometer(1000)

# Driving the car
my_car.drive(100)

# Checking odometer reading
print(my_car.get_odometer_reading())  # Output: 1100
