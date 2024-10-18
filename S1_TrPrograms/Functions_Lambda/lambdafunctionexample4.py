
# Example list
my_list = [1, 2, 3, 4, 5]
 
# Use lambda to filter out even numbers from the list
new_list = list(filter(lambda x: x % 2 != 0, my_list))
 
# Print the new list
print(new_list)
