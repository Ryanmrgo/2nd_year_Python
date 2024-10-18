from Student import Student
from Faculty import Faculty

class TeachingAssistant(Faculty,Student):
     ''' Defining the multiply inherited class with its structural '''
     ''' and behavioral attributes '''

     # Constructor of the class
     def __init__(self, *ta_data):
          ''' Initializes the variables assuming all 6 values are provided
               Make necessary checks to ensure index out of range does not occur '''
          Faculty.__init__(self,ta_data[0],ta_data[1],ta_data[2],ta_data[3],ta_data[4])
          Student.setRollNumber(self,ta_data[5])


# Main program section
if __name__ == "__main__":
     print()
     print("Creating Teaching Assistant object")
     print()
     ta1 = TeachingAssistant("Asha","Kapoor","March 6, 1999","Bangkok, Thailand","YYY-099","XXX-EEE-S001",)
     print("\tFirst name of teaching assistant: " + ta1.getFirstName())
     print("\tLast name of teaching assistant:" + ta1.getLastName())
     print("\tDate of birth of teaching assistant: " + ta1.getDOB())
     print("\tAddress of teaching assistant: " + ta1.getAddress())
     print("\tFaculty ID of teaching assistant: " + ta1.getFacultyID())
     print("\tRoll number of teaching assistant: " + ta1.getRollNumber())
     print()

