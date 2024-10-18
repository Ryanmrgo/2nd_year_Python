# CSE 1040 - Lecture 11 - Example 3
# Example illustrating collection-controlled construct in Python

# Using collection-controlled loop - iterating over a tuple using range
print()
gradelist = (['A',4.0],['A-',3.7],['B+',3.4],['B',3.0])
numb_elements = len(gradelist)
print("Iterating over a tuple: ")
for i in range(numb_elements):
     print("Grade point of grade " + gradelist[i][0] + " is " + str(gradelist[i][1]))
print()

# Using collection-controlled loop - iterating over a list directly on the list
gradelist = [['A',4.0],['A-',3.7],['B+',3.4],['B',3.0]]
print("Iterating over a list: ")
for i in gradelist:
     print("Grade point of grade " + i[0] + " is " + str(i[1]))
print()

# Using collection-controlled loop - iterating over a string directly on the string
vowels = "AEIOU"
print("Iterating over a string: ")
for i in vowels:
     print("Vowel is " + i)
print()

# Using collection-controlled loop - iterating over a set directly on the set
vowels = {"A","E","I","O","U"} # Defining a set
print("Iterating over a set: ")
for i in vowels:
     print("Vowel is " + i)
     
print()
print()
