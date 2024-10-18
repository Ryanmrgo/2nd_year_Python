# Working with classes in Python - Part 1

import fraction1 as fc

# Creating objects of class Fraction
print('================================================================')
f1 = fc.Fraction() # No arguments
f2 = fc.Fraction(10) # Setting numerator
f3 = fc.Fraction(10,2) # Setting both numerator and denominator
f4 = fc.Fraction() # No arguments

print(str(f1))
print(f2)
print(f3)
print(f4.getFraction())

f4.setFraction(20,4)
print(f4)

#print('=================================================================')


