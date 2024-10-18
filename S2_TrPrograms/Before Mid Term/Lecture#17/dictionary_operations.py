# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Original Dictionary:")
print(my_dict)
print("Getting associated value of key:")
print(my_dict['name'])
keys=my_dict.keys()
print(list(keys))
values=my_dict.values()
print(list(values))


'''
# Changing the value of an existing key
my_dict['age'] = 26
print("Modified Dictionary:")
print(my_dict)

# Adding a new key-value pair
my_dict['occupation'] = 'Software Engineer'

print("Modified Dictionary:")
print(my_dict)

# Removing a key-value pair
del my_dict['city']

print("Dictionary after removing 'city':")
print(my_dict)

#Duplicate key values will overwrite existing values:
print("Duplicate key values will overwrite existing values:")
thisdict ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1985,
  "year": 2020
}
print(thisdict)
print('Length of dictionary:',len(thisdict))
'''
