from Person import Person
class Student(Person):
     ''' Defining the sub class Class with its structural '''
     ''' and behavioral attributes '''

     # Constructor of the class
     def __init__(self, *student_data):
          ''' Initializes the variables assuming all 5 values are provided
               Make necessary checks to ensure index out of range does not occur '''
          Person.__init__(self,student_data[0],student_data[1],student_data[2],student_data[3])
          self.__rollNumber = student_data[4]           

     def setRollNumber(self,rollNumber):
          self.__rollNumber = rollNumber
          
     def getRollNumber(self):
          return self.__rollNumber

# Main program section
if __name__ == "__main__":
     print()
     print("Creating Student object")
     print()
     s1 = Student("Tom","Blake","January 1, 1999","New York, USA","XXX-EEE-S001")
     print("\tFirst name of student: " + s1.getFirstName())
     print("\tLast name of student: " + s1.getLastName())
     print("\tDate of birth of student: " + s1.getDOB())
     print("\tAddress of student: " + s1.getAddress())
     print("\tRoll number of student: " + s1.getRollNumber())
     print()
