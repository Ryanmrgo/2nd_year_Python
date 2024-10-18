# Lecture 10 Example using a set in Python

# Creating an empty set
print()
mySet = set()
takeInput = True
while takeInput:
     setMember = int(input('Enter a positive integer, 0 to quit: '))
     if setMember == 0:
          takeInput = False
     else:
          mySet.add(setMember)
print(mySet)
'''
# Ways in which you can initialize a set
print()
mySet.clear()
print('Printing the set after using clear function ...')
print(mySet)
'''
'''
print()
print('Printing after initializing with the set function ...')
mySet = set([34.6,32.6,33.4,45.6])
print(mySet)
'''
'''
print()
print('Printing after initializing with {}...')
mySet = {34.6,32.6,33.4,45.6}
print(mySet)
'''
