# CSE 2040 - Lecture 17 - Example 1
# Example illustrating creation of a dictionary and iterating

# Declaring an empty dictionary
print()
print('Creating an empty dictionary')
dictionary = {}
print('\tEmpty dictionary created -', dictionary)

# Adding key:value pairs to an empty dictionary
print()
print('Adding key:value pairs of sports personalities ...')
dictionary['Federer'] = 'Tennis' 
dictionary['Maradona'] = 'Football'
dictionary['Tendulkar'] = 'Cricket'
dictionary['Bolt'] = 'Athletics'
dictionary['Hamilton'] = 'Racing'
dictionary['Ali'] = 'Boxing'

# Print number of key:value pairs in the dictionary
print()
print('Added',len(dictionary), 'key:value pairs to the dictionary')

# Printing the dictionary
print()
print('Values of the dictionary:')
print(dictionary)

# Iterating and printing the keys of dictionary
print()
print('Iterating over keys of dictionary')
for key in dictionary:
     print("Key is: " + key);
     
# Iterating and printing key:value pairs of dictionary
print()
print('Iterating over key:value pairs of dictionary')
for key,value in dictionary.items():
     print(key + ' plays ' + value)

