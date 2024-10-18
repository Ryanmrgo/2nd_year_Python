#Python program to understand instance variable

class Sample:
#instance vars sample
    def __init__(self):
        self.x=10
#This is and instance method
    def modify(self):
        self.x+=10
        
#create 2 instances
s1=Sample()
s2=Sample()
print('-----------')
print('before modify',s1.x)
print('before modify',s2.x)
#modify in s1
s1.modify()
#s2.modify()
print('-----------')
print('-----------')
print('-----------',s1.x)
print('-----------',s2.x)



