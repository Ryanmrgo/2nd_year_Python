# CSE 2040 - Lecture 16 - Example 1
# Example illustrating what evaluates to False by default

print()
# Defining a few variables
name = ""
names = []
months = ()
number = 0
marks = 0.0
dont_know = None

if (name):
     print("I know my name")
else:
     print("LOL! I do not know my name!")

print()
if (names):
     print("I know there are names in the list")
else:
     print("It is an empty list!")

print()
if (months):
     print("There are months in the tuple")
else:
     print("There are no months in the tuple!")

print()
if (number):
     print("The number is not zero")
else:
     print("AH! The number is zero!")

print()
if (marks):
     print("My marks is NOT zero")
else:
     print("Oh! My marks ARE zero!")

print()
if (dont_know):
     print("Yes, I do know something")
else:
     print("Noo! I do not know anything!")

print()
print()
