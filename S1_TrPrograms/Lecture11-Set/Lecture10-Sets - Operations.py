# Lecture10-Example using a set in Python

# Demonstrating add operation
print()
mySet = set()
member = 100
print('Adding an element to a set ...')
mySet.add(member)
print(mySet)

print()
members = (100, 200)
print('Adding a tuple to a set ...')
mySet.add(members)
print(mySet)
member2=(100,200,300)
mySet.add(member2)
print(mySet)
# Demonstrating copy operation
print()
originalSet = {'a', 'e', 'i', 'o', 'u'}
print(originalSet)
copiedSet = originalSet.copy()
originalSet.clear()
print('Copying a set to another ...')
print(copiedSet)

print()
originalSet = {'aa', 'ee', 'ii', 'oo', 'uu'}
print(originalSet)
copiedSet = originalSet
originalSet.clear()
print('Assigning a set to another ...')
print(copiedSet)

# Demonstrating difference operation
setX = {'a', 'e', 'i', 'o', 'b', 'u', 'z'}
setY = {'b'}
setZ = {'z'}
newSet = setX.difference(setY).difference(setZ)
print()
print('Showing difference of sets using different operation ...')
print(newSet)
print(setX - setY - setZ)

print('Showing difference of two sets ...')
setX = {(10,20,30), (20,30,40), (30,40,50)}
setY = {(10,20), (30,40), (30,50)}
print()
print(setX - setY)
