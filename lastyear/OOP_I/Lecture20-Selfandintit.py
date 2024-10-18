#Lecture 25- Diff between init and self
class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
      # print('test for consturctor',self)
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   def get_area(self):
       #print('test for getarea',self)
       return self.length * self.breadth
   def calculate_cost(self):
       #print('test for calculate cost',self)
       area = self.get_area()
       return area * self.unit_cost
# breadth = 120 units, length = 160 units, 1 sq unit cost = Ks 2000
r = Rectangle(160, 120, 2000)
#print('test for object',r)
print("Area of Rectangle: %s sq units" % (r.get_area()))
print("cost of Rectangle:  %s  ks" % (r.calculate_cost()))

print(r.get_area())
print(r.calculate_cost())
