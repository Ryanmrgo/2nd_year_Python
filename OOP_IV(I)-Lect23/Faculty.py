# CSE 2040 - Lecture 23 

from Person import Person

# Sub class Faculty

class Faculty(Person):
     ''' Defining the sub class Faculty with its structural '''
     ''' and behavioral attributes '''

     # Constructor of the class
     def __init__(self, *faculty_data):
          ''' Initializes the variables assuming all 5 values are provided
               Make necessary checks to ensure index out of range does not occur '''
          Person.__init__(self,faculty_data[0],faculty_data[1],faculty_data[2],faculty_data[3])
          self.__facultyID = faculty_data[4]           

     def getFacultyID(self):
          return self.__facultyID
     
# Main program section
if __name__ == "__main__":
     print()
     print("Creating Faculty object")
     print()
     f1 = Faculty("Kane","Hawkins","December 12, 1982","North Carolina, USA","YYY_009")
     print("\tFirst name of faculty: " + f1.getFirstName())
     print("\tLast name of faculty: " + f1.getLastName())
     print("\tDate of birth of faculty: " + f1.getDOB())
     print("\tAddress of faculty: " + f1.getAddress())
     print("\tFaculty ID of faculty: " + f1.getFacultyID())
     print()
