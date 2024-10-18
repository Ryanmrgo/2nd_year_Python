'''
#Demonstrating multiple inheritance
class Dog:
    def sound(self):
        print("Woof!")

class Bird:
    def sound(self):
        print("Tweet!")

class DogBird(Dog, Bird):
    pass

my_pet = DogBird()
my_pet.sound()  
'''
'''Demonstrating MRO: hierarchy '''
'''
class A:
    def greet(self):
        print("Greetings from class A")
        
class B(A):
    def greet(self):
        print("Greetings from class B")
        super().greet()

class C(A):
    def greet(self):
        print("Greetings from class C")
        super().greet()
         
class D(B, C):
    pass

obj_D = D()
obj_D.greet()
'''
'''Since D doesn't have its own greet() method, Python checks class B.
    Class B has its own greet() method, but it also calls super().greet(), which means Python will look for the next method in the MRO.
    Next, Python checks class C.
    Class C also has its own greet() method, but it also calls super().greet().
    Since there are no more classes to check in the MRO after C, Python goes back to B,
    and the super().greet() call there resolves to the greet() method of class A.'''
#Diamond problem in Python with an example:
'''
class A:
    def greet(self):
        print("Greetings from class A")

class B(A):
    def greet(self):
        print("Greetings from class B")

class C(A):
    def greet(self):
        print("Greetings from class C")

class D(B, C):  # Diamond problem
    pass

obj_D = D()
obj_D.greet()
'''
class A:
    def greet(self):
        print("Greetings from class A")

class B(A):
    def greet(self):
        print("Greetings from class B")

class C(A):
    def greet(self):
        print("Greetings from class C")

class D(B, C):
    def greet(self):
        B.greet(self)  # Explicitly call greet method from class B
        C.greet(self)  # Explicitly call greet method from class C

# Creating an instance of class D
obj_D = D()

# Calling the greet method
obj_D.greet()



