class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def speak(self):  # Method overriding
        print("Dog barks")


class Cat(Animal):
    def __init__(self, name):
        super().__init__("Cat")
        self.name = name

    def speak(self):  # Method overriding
        print("Cat meows")


dog = Dog("Buddy")
print(dog.species)
print(dog.name)
dog.speak()  # Output: "Dog barks"

cat = Cat("Whiskers")
print(cat.species)
print(cat.name)
cat.speak()  # Output: "Cat meows"
