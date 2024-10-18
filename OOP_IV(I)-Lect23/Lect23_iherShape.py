'''
class Shape:
    color=(0,0,0)
    #def __init__(self):
        #self.color=(0,0,0)
class Rectangle(Shape):
    def __init__(self,w,h):
        #Shape.__init__(self)
        self.width=w
        self.height=h
    def area(self):
        return self.width*self.height
    def display(self):
        print('area is',self.width*self.height)
r1=Rectangle(10,5)
print(r1.width)
print(r1.height)
print(r1.area())
print(r1.color)
print(Shape.color)
#r1.display()
'''

class Shape:
    def __init__(self):
        self.color=(0,0,0)
class Rectangle(Shape):
    def __init__(self,w,h):
       super().__init__()
       #super().__init__(self)
       #super().area()
       self.width=w
       self.height=h
    def area(self):
        return self.width*self.height
r1=Rectangle(10,5)
print(r1.width)
print(r1.height)
print(r1.area())
print(r1.color)
        



