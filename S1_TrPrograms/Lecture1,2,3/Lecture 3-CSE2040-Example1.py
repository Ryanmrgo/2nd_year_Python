# CSE 2040 - Lecture 5 - Example 
# Example illustrating assignments and identify of variables in Python

# Assign same values to different variables

number1 = 17
number2 = number1

name1 = "June"
name2 = name1

print()
print(number1)
print(number2)

print()
print(name1)
print(name2)

# Let us check the identity of the four variables
print()
print("Id of number1", id(number1))
print()
print("Id of number2", id(number2))
print()
print("Id of name1", id(name1))
print()
print("Id of name2", id(name2))

number2 = 6

name2 = "July"

print()
print("After changing values of number2 and name2 ...")

print()
print(number1)
print(number2)

print()
print(name1)
print(name2)

print()
print("Id of number1", id(number1))
print()
print("Id of number2", id(number2))
print()
print("Id of name1", id(name1))
print()
print("Id of name2", id(name2))
