#instance methods to process data of object
class Student:
#this is  constructor
    def __init__(self,n='',m=0):
        self.name=n
        self.marks=m
#This is and instance method
    def display(self):
        print('Hi',self.name)
        print('my marks are',self.marks)
        #to calculate grades based on marks
    def calculate(self):
        if(self.marks>=600):
            print ('you got the first grade')
        elif(self.marks>=500):
            print ('you got the second grade')
        elif(self.marks>=300):
            print ('you got the third grade')
        else:
            print ('you are failed')
#create an instance with some data from the keyboards
n=int(input('How many Students'))
i=0
while(i<n):
    name=input('Enter name')
    marks=int(input('Enter marks'))
    #create Student class instance and store data
    s=Student(name,marks)
    s.display()
    s.calculate()
    i+=1
print('---------------')




