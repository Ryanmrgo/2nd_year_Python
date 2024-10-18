'''
class A:
    a=1
    b=2
    def method1(cls):
        print(cls.a)
        print(cls.b)
class B(A):
    c=3
    def method2(cls):
        print(cls.c)
b=B()
b.method2()
#b.method1()
'''

class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak() 
