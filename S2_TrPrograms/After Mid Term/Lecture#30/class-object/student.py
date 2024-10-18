from teacher import Teacher
'''Demonstrating inheritance'''

class Student(Teacher):

    def setmarks(self,mark):
        self.mark=mark

    def getmarks(self):
        return self.mark

s=Student()

s.setid("001")
s.setname("Rakesh")
s.setaddress("HNO-22, Ameerpet, Hyderabad")
s.setmarks(40)

print("ID: ",s.getid())
print("Name: ",s.getname())
print("Address: ",s.getaddress())
print("Mark: ",s.getmarks())
