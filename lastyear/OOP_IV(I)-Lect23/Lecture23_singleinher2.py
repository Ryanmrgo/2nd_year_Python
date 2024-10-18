# parent class
class Student():
   # constructor of parent class
   def __init__(self, name, enrollnumber):
      self.name = name
      self.enrollnumber = enrollnumber
   def display(self):
      print(self.name)
      print(self.enrollnumber)
# child class
class College( Student ):
   def __init__(self, name, enrollnumber, admnyear, branch):
      self.admnyear = admnyear
      self.branch = branch
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)
# creation of an object for base/derived class
obj = College('Rohit',42414802718,2018,"CSE")
obj.display()
