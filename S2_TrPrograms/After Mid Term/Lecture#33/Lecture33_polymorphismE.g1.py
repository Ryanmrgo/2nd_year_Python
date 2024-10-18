#Polymorphism: Duck Typing
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"

# Function that accepts any Animal and makes it speak
def make_animal_speak(animal):
    print(animal.speak())

# Creating instances of different animals
dog = Dog()
cat = Cat()
duck = Duck()

# Making each animal speak using the same function
make_animal_speak(dog)   # Output: Woof!
make_animal_speak(cat)   # Output: Meow!
make_animal_speak(duck)  # Output: Quack!

'''We create instances of Dog, Cat, and Duck, and pass them
to the make_animal_speak() function.
Despite being different types of animals, they all have a speak()
method due to polymorphism, and thus,
they all can "speak" when the function is called.'''

