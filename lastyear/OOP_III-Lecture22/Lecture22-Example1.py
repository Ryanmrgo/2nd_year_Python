#illustration of creating a class in python with input from the user
class Student:
    #student class
    stuCount=0 #class var
    def __init__(self): #constructor
        
        self.name=input('Enter student name')
        self.rollno=input('Enter Roll no')
        Student.stuCount+=1
    def displayStudent(self):# display information
        print('Name',self.name,'Roll no',self.rollno)
stu1=Student()
stu2=Student()
stu3=Student()
stu1.displayStudent()
stu2.displayStudent()
stu3.displayStudent()
s=Student.stuCount # using class variable,format is classname.classvariablename
print("The total no of student is",s)

        
        
