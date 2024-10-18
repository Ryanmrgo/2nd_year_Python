#Accessor and mutator methods
class Student:
#this mutator method
        def setName(self,name):
            self.name=name
#this accessor method
        def getName(self):
            return self.name
    #this mutator method
        def setMarks(self,marks):
            self.marks=marks
#this accessor method
        def getMarks(self):
            return self.marks

#create an instance with some data from the keyboards
n=int(input('How many Students'))
i=0
while(i<n):
    #create student class instance
    s=Student()
    name=input('Enter name')
    s.setName(name)
    marks=int(input('Enter marks'))
    s.setMarks(marks)
    #retrive data from Student class instance
    print('Student name is',s.getName())
    print('Your marks is',s.getMarks())
    i+=1
    print('---------')




