class Sample:
#class var
    x=10
    y=20
#class method
    @classmethod       
    def modify(cls):
        cls.x+=10
        cls.y+=10
        
print('Accessing class level method and attribute')

Sample.modify()
print('Test for class variable',Sample.x)
print('-----------')

s1=Sample()
s2=Sample()

print('Accessing class level method and attribute using class instance')
s1.modify()
print('-----------',s1.x)
print('-----------',s2.x)

