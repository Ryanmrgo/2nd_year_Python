# CSE 2040 - Lecture 28 - Example 1

# Python program using the fraction module

import fraction as f

# Creating objects of class Fraction
print('================================================================')
f1 = f.Fraction() # No arguments
f2 = f.Fraction(10) # Setting numerator
f3 = f.Fraction(10,2) # Setting both numerator and denominator
f4 = f.Fraction() # No arguments

# String version of ojects f1, f2 and f3 are printed
# Because we have defined the method __str__ in class Fraction
print(f1)
print(f2)
print(f3)

# Method getFraction() is called on object f4, returning an anonymous object
# String version of the anonymous object is printed
# Because we have defined the method __str__ in class Fraction
print(f4.getFraction())

# Using setFraction values for f4 object are changed and then printed
f4.setFraction(20,4)
print(f4)

# Printing the number represented by the fraction by calling convert method
print('=================================================================')
print()
print('Fraction ' + str(f3) + ' converted to number - ' + str(f3.convert()))

# Adding fraction f3 and f4
print('=================================================================')
print()
f5 = f3.addFraction(f4)
print(f5)
print('Fraction ' + str(f5) + ' converted to number - ' + str(f5.convert()))

print('=================================================================')
print()
f6 = f5.addFractions(f2,f3,f4)
print('Fraction ' + str(f6) + ' converted to number - ' + str(f6.convert()))
print('=================================================================')
