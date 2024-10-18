#to create abstract class and sub classes which implement the abstract method of the abstract class
from abc import ABC, abstractmethod

class Myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass

class Sub1(Myclass):
    def calculate(self,x):
        print('square value: ',x*x)

import math
class Sub2(Myclass):
    def calculate(self,x):
        print('square root: ',math.sqrt(x))
        
class Sub3(Myclass):
    def calculate(self,x):
        print('cube value: ',x**3)

obj1=Sub1()
obj1.calculate(3)
obj2=Sub2()
obj2.calculate(3)
obj3=Sub3()
obj3.calculate(3)
