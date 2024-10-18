# CSE 2040 - Lecture 17 - Example 2
# Example illustrating more about use of dictionaries

# Declaring an empty dictionary
dictionary1 = {}
dictionary2 = {'match':'game', 'analytical':'systematic', 'good':'acceptable'}
dictionary3 = {"A":4, "A-":3.7, "B+":3.4, "B":3, "B-":2.7, "C+":2.4, "C":2, "D":1, "F":0}

# Add key:value pair to a dictionary
dictionary2['study'] = 'learn'
print()
print('After adding ...')
print(dictionary2)

# Add key:value pair for an existing key
dictionary2['match'] = 'competition'
print()
print('After adding again...')
print(dictionary2)

# Extract the value for a given key
print()
print('The value of analytical is ' + dictionary2['analytical'])

# Delete a key: value pair
print()
del dictionary2['good']
print('After deletion ...')
print(dictionary2)

# Get a list of keys in unsorted order
print()
print(list(dictionary3.keys()))

# Get a list of keys in sorted order
print()
print(sorted(dictionary3.keys()))

# Find if a key is in the dictionary
print()
print('Is good in the dictionary?: ' + str('good' in dictionary2))

print()
if 'B+' in dictionary3:
     print('B+ is in the dictionary')
else:
     print('B+ is not in the dictionary')

