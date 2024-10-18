#Lecture 21, CSE-2040
class MyClass:
     def __init__(self):
          self.a = 100
          self._b = 200
          self.__c = 300

     def setA(self):
          print('Inside public method')

     def _setB(self):
          print('Inside protected method')

     def __setC(self):
          print('Inside private method')

     def getA(self):
          return self.a

     def getB(self):
          return self._b

     def getC(self):
          return self.__c

# Create an object of MyClass
mc1 = MyClass()

# Calling the public method
print('setter called',mc1.setA())

# Calling the protected method
print('setter called',mc1._setB())

# Calling the private method - throws an error, name mangling required
#mc1.setC()

mc1._MyClass__setC()


# Changing the value of the public data attribute before printing
mc1.a = 102
print()
print('a is',mc1.a)
print()

# Trying to change the value of the protected data attribute before printing
mc1.b = 104

print()
#print('b is',mc1.b) # Does not print the value of the data attribute contained in the class
print()

# Trying to change the value of the private data attribute before printing
mc1.c = 106
print()

#print('c is',mc1.c) # Does not print the value of the data attribute contained in the class
print()

# Changing the private data attribute will result an error. Comment and try again
mc1.__c = 2101 

# Good programming practice is to always use the getter methods to get the values of attributes of a class
print('getter for a',mc1.getA())

print('getter for b',mc1.getB())

print('getter for c',mc1.getC())
print()

