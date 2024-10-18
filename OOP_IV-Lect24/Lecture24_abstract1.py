'''
class MyClass:
    def calculate(self,x):
        print('Square value',x*x)
obj1=MyClass()
obj1.calculate(2)
obj2=MyClass()
obj2.calculate(3)
obj3=MyClass()
obj3.calculate(4)
'''
#abstrct class example
import math
from abc import ABC,abstractmethod

class MyClass(ABC):
    def calculate(self,x):
        pass
        
class subclass1(MyClass):
    def calculate(self,x):
        print('Square value',x*x)
    

class subclass2(MyClass):
    def calculate(self,x):
        print('Square root value',math.sqrt(x))

class subclass3(MyClass):
    def calculate(self,x):
        print('Cube value',x*x*x)

obj1=subclass1()
obj1.calculate(2)
obj2=subclass2()
obj2.calculate(3)
obj3=subclass3()

'''
obj3.calculate(4)
