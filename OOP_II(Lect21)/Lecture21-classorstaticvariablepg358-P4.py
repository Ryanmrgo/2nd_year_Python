#Python program to understand class variable or static vars

class Sample:
#this is a class var
            x=10
#This is a class method
            @classmethod       
            def modify(cls):
                cls.x+=10
        
#create 2 instances
s1=Sample()
s2=Sample()
print('Test for class variable',Sample.x)
print('-----------')
print('-----------',s1.x)
print('-----------',s2.x)
#modify in s1
s1.modify()
print('-----------')
print('-----------')
print('-----------',s1.x)
print('-----------',s2.x)



