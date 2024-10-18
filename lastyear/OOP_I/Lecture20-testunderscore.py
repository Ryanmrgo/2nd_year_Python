class Number:

     def __init__(self, x1, x2):
          self.x = x1 # x is public data attribute
          self.__y = x2 # y is private data attribute

     def getX(self):
          return self.x

     def getY(self):
          return self.__y

number = Number(100,200)
print(number.x) # Defined as public in class Number, hence can be used directly
number.x = number.x + 10
print(number.x) # Defined as public in class Number, hence can be changed too
print(number.getY()) # Defined as private in class Number, hence can only be know through a method
print(number.getX()) # Can be known even using the method but the changed will be printed now
#print(number.y) 
print(number._Number__y)#Name Mangling required
#print(number._Number__y)# Not allowed as defined as private in class Number
