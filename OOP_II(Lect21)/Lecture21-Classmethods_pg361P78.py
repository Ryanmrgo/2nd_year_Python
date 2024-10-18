'''
#understanding class methods
class Bird:
    #this is a class var
    wings=2
    #this is a class method
    @classmethod
    def fly(cls,name):

        print('{} flies with {} wings'.format(name,cls.wings))
#display infor for two birds
Bird.fly('Sparrow')
Bird.fly('Piegon')
'''


#understanding the static methods
class MyClass:
    #this is class var or static var
    n=0
    #constructor that increments n when an instance is created
    def __init__(self):
        MyClass.n=MyClass.n+1
    #this is the static method to display the number of instances
    #@staticmethod
    def noObjects():
        print('no.of instances created',MyClass.n)

#create 3 instances
obj1=MyClass()
obj2=MyClass()
obj3=MyClass()
MyClass.noObjects()
'''

#understanding static method to find the square root value
import math
class Sample:
    #@staticmethod
    def calculate(x):
        result=math.sqrt(x)
        return result
#accept a number from keyboard
num=float(input('Enter a number'))
#call the static method and pass num
res=Sample.calculate(num)
print('The Square root of {} is {:.2f}'.format(num,res))
'''




    







        

