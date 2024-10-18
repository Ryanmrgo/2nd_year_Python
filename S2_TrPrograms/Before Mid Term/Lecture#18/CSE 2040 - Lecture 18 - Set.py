# CSE 2040 - Lecture 18 - Example 1
# Example illustrating definition of set and operations on set

# Defining set
print()
set1 = {1,2,3}
set2 = {3,4,5}

print("Union of set1 and set2:")
print(set1 | set2)
print(set1.union(set2))

print()
print("Adding an element to a set:")
set1.add(7)
print(set1)

print()
print("Removing an element to a set:")
set2.discard(4)
print(set2)

print()
print()
