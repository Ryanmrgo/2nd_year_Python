# CSE 2040 - Lecture 16 - Example 2
# Example illustrating different forms of if statement in Python

print()
a = 10
b = 16
c = 12

# Normal nested if statements
print("Using normal nested if construct")
if (a == b):
     print("a and b are the same!")
else:
     if (a == c):
          print("a and c are the same but a and b are not the same")
     else:
          print("a, b and c are different")

# Following nested if the same as above but compact
print()
print("Using Python nested if construct")
if (a == b):
     print("a and b are the same!")
elif (a == c):
     print("a and c are the same but a and b are not the same")
else:
     print("a, b and c are different")

# Using ternary if
max = a if (a > b) else b
print()
print(max)


# Using ternary if in a print statement 
print()
print(a if(a > b) else b)

