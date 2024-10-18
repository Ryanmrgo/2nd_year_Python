# Printing the object reference
# Both self and number have the same reference
# As number is the object that is constructed

class Number:

     def __init__(self,x1,x2):
          self.x = x1
          self.y = x2
          #print(self)

number = Number(1000,2000)
#print(number)
print(number.x)
print(number.y)


