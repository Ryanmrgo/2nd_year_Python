# CSE 2040 - Lecture 23 - Example 1

# Base class Person

class Person:
     ''' Defining the base class Person with its structural '''
     ''' and behavioral attributes '''

     # Constructor of the class
     def __init__(self, *person_data):
          ''' Initializes the variables assuming all 4 values are provided
               Make necessary checks to ensure index out of range does not occur '''
          self.__firstName = person_data[0]
          self.__lastName = person_data[1]
          self.__dob = person_data[2]
          self.__address = person_data[3]

     def getName(self):
          return self.__firstName + " " + self.__lastName

     def getFirstName(self):
          return self.__firstName

     def getLastName(self):
          return self.__lastName

     def getDOB(self):
          return self.__dob

     def getAddress(self):
          return self.__address

# Main program section
if __name__ == "__main__":
     print()
     print("Creating Person object")
     print()
     p1 = Person("Aretha","Franklin","March 25, 1942","Memphis, USA")
     print("\tFirst name of person: " + p1.getFirstName())
     print("\tLast name of person: " + p1.getLastName())
     print("\tDate of birth of person: " + p1.getDOB())
     print("\tAddress of person: " + p1.getAddress())
     print()
     p2 = Person("ma ma","aung","June 12, 1972","Monywa, Myanmar")
     print("\tFirst name of person: " + p2.getFirstName())
     print("\tLast name of person: " + p2.getLastName())
     print("\tDate of birth of person: " + p2.getDOB())
     print("\tAddress of person: " + p2.getAddress())
     print()
