
#inner or nested class example
class Person:
    def __init__(self):
        self.name='Phway Phway'
        #self.age=23
        self.db=self.Dob()
    def display(self):
        print('Name=',self.name)
        #print('Age=',self.age)
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1988
        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
#creating person class object
p=Person()
p.display()
#creating inner class object
x=p.db
x.display()
print(x.dd)
print(x.yy)
print(x.mm)



'''
#inner or nested class example-vesion2
class Person:
    def __init__(self):
        self.name='Charles'
        
    def display(self):
        print('Name=',self.name)
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1988
        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))

#creating Person class object
p=Person()
p.display()
x=Person().Dob()
x.display()
print(x.yy)
'''




        
