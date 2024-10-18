# Working with classes in Python - Part 1

# Defintion of class Fraction

class Fraction:
     ''' This class creates a Fraction class and sets and get the numerator
          and the denominator of a fraction '''

     def __init__(self, num=0, den=1):
          ''' Constructor for the class to set the numerator
               and the denominator '''
          self.numerator = num
          self.denominator = den

     def setFraction(self, num=0, den=1):
          ''' Setter function to set the values for numerator
               and denominator '''
          self.numerator = num
          self.denominator = den         
     
     def getFraction(self):
          ''' Getter function to get the fraction '''
          tempFraction = Fraction(self.numerator, self.denominator)
          return tempFraction

     def getDenominator(self):
          return self.denominator

     def getNumerator(self):
          return self.numerator

     def __str__(self):
          ''' Converting the attributes to a string enabling easy display '''
          return str(self.numerator) + '/' + str(self.denominator)

     def convert(self):
          ''' Converting the fraction to a number '''
          return self.numerator/self.denominator

    
               
 
