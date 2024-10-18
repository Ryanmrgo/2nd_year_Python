# CSE 2040 - Lecture 14 - Example 3
# Example illustrating list-specific functions

print()
print()
# Defining a list
roll_numbers = ["CSE-001","CSE-002","CSE-003","CSE-004"]
print()
print("Initial list:")
print(roll_numbers)

# Appending (adding) a single element at the end of the list
roll_numbers.append("CSE-005")
print()
print("After appending:")
print(roll_numbers)

# Extending the list using a sequence
new_roll_numbers = ["CSE-006","CSE-007"]
roll_numbers.extend(new_roll_numbers)
print()
print("After extending:")
print(roll_numbers)

# Appended two more elements
roll_numbers.append("CSE-001")
roll_numbers.append("CSE-002")

# Finding the number of times an element occurs in a list
print()
print("Count of element CSE-001:")
print(roll_numbers.count("CSE-001"))

# Finding the first occurrence of an element in a list
print()
print("Index where element CSE-002 occurs:")
print(roll_numbers.index("CSE-002"))

# Inserting an element in a list at an index
roll_numbers.insert(len(roll_numbers),"CSE-060")
print()
print("After inserting a new element after a given index:")
print(roll_numbers)

# Removing an element from a list
roll_numbers.remove("CSE-001")
print()
print("After removing an element from the list:")
print(roll_numbers)

# Reversing the elements of a list
roll_numbers.reverse()
print()
print("Reversing the elements in the list:")
print(roll_numbers)

# Sorting the elements in a list
roll_numbers.sort()
print()
print("Sorting the elements in the list:")
print(roll_numbers)

#After pop() the last element in the list
roll_numbers.pop()
print("After pop() the last element in the list:")
print(roll_numbers)

print()
print()
