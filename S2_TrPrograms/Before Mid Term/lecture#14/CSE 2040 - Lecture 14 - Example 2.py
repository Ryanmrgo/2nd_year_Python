# CSE 2040 - Lecture 14 - Example 2
# Example illustrating functions of lists and tuples

# Defining two tuples
vowels_small = ("a","e","i","o","u")
vowels_big = ("A","E","I","O","U")

print()
print()
# Printing maximum value in the tuple
print(max(vowels_small))

print()
# Printing minimum value in the tuple
print(min(vowels_small))

print()
# Converting a tuple to a list
vowels_big_list = list(vowels_big)
print(vowels_big_list)

print()
# Converting a list to a tuple
roll_numbers = ["CSE-001","CSE-002","CSE-003","CSE-004"]
roll_numbers_tuple = tuple(roll_numbers)
print(roll_numbers_tuple)

print()
print()
