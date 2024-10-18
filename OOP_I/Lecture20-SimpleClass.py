#simple class in python
#Instance variables and instance methods
class Student:
#this is special method called constructor
    def __init__(self):
        print('test for self constructor',self)
        self.name="mama"
        self.age=20
        self.marks=900
#This is and instance method
    def printStudentinfo(self):
        print('test for self simple fun',self)
        print('I am',self.name)
        print('my age is',self.age)
        print('my marks are',self.marks)
#create an instance to Student class
s1=Student()
print('test for s1',s1)

#call the method using instance
s1.printStudentinfo()



