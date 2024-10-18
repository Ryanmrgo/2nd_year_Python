# CSE 2040 - Lecture 28 - Example 1

# Defintion of class Fraction

class Fraction:
     ''' Implementation of fraciton '''
     
     def __init__(self, num=0, den=1):
          ''' Constructor for the class to set the numerator
               and the denominator '''
          self.__numerator = num
          self.__denominator = den

     def setFraction(self, num=0, den=1):
          ''' Setter function to set the values for numerator
               and denominator '''
          self.__numerator = num
          self.__denominator = den         
     
     def getFraction(self):
          ''' Getter function to get the fraction '''
          tempFraction = Fraction(self.__numerator, self.__denominator)
          return tempFraction

     def getDenominator(self):
          return self.__denominator

     def getNumerator(self):
          return self.__numerator

     def __str__(self):
          ''' Converting the attributes to a string enabling easy display '''
          return str(self.__numerator) + '/' + str(self.__denominator)

     def convert(self):
          ''' Converting the fraction to a number '''
          return self.__numerator/self.__denominator

     def addFraction(self,fraction):
          '''Adding fraction provided as a parameter with this fraction (self) '''
          denominator = self.__denominator * fraction.__denominator
          numerator1 = int(denominator / self.__denominator) * self.__numerator
          numerator2 = int(denominator / fraction.__denominator) * fraction.__numerator
          tempFraction = Fraction((numerator1+numerator2), denominator)
          return tempFraction
     
     def addFractions(self,*fractions):
          '''Adding any number of fractions'''
          denominator = self.__denominator
          for fraction in fractions:
               # Method getFraction() can also be used to get the denominator
               denominator = denominator * fraction.getDenominator() 
          numerator = int(denominator / self.__denominator) * self.__numerator
          for fraction in fractions:
               numerator = numerator + int(denominator / fraction.__denominator) * fraction.__numerator
          tempFraction = Fraction(numerator, denominator)
          return tempFraction

