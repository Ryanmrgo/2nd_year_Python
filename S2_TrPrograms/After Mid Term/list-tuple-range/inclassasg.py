# Byte sequence
byte_sequence = bytes([1, 1, 2, 3, 5, 8, 13, 21])

# Byte array
byte_array = bytearray([1, 1, 2, 3, 5, 8, 13, 21])

# List
my_list = ["Yangon", "Mandalay", "Bangalore", "New York"]

# Tuple
my_tuple = (1, "Jack", 28, 2, "Rob", 30, 3, "Jill", 29)

# Common functions
# Length
print("Length:")
print("Byte Sequence:", len(byte_sequence))
print("Byte Array:", len(byte_array))
print("List:", len(my_list))
print("Tuple:", len(my_tuple))

# Concatenation
print("\nConcatenation:")
print("byte_array + byte_sequence:", byte_array + bytes(byte_array))
print("byte_sequence + byte_array:", byte_sequence + bytearray(byte_sequence))
print("List + Tuple:", my_list + list(my_tuple))  # Convert tuple to list for concatenation
print("Tuple + List:", my_tuple + tuple(my_list))

# Repetition
print("\nRepetition:")
print("Byte Sequence * 2:", byte_sequence * 2)
print("Byte Array * 2:", byte_array * 2)
print("List * 2:", my_list * 2)
print("Tuple * 2:", my_tuple * 2)

# Contains
print("\nContains:")
print("Byte Sequence contains 3:", 3 in byte_sequence)
print("'Rob' in Tuple:", 'Rob' in my_tuple)

# Not contains
print("\nNot Contains:")
print("Byte Array does not contain 7:", 7 not in byte_array)
print("'Bangalore' not in List:", 'Bangalore' not in my_list)

# Indexing
print("\nIndexing:")
print("First element of Tuple:", my_tuple[0])
print("Last element of List:", my_list[-1])

# Slicing
print("\nSlicing:")
print("Slice of Byte Sequence:", byte_sequence[2:5])
print("Slice of Byte Array:", byte_array[1:6])
print("Slice of List:", my_list[1:3])
print("Slice of Tuple:", my_tuple[3:6])

# Using extend vs append
new_elements = ["Tokyo", "London"]
item=[1,2]

# Using extend
my_list.extend(new_elements)
print("\nUsing extend:")
print("Extended List:", my_list)
#my_tuple.extend(new_elements)
#byte_sequence.extend(item)
byte_array.extend(item)
print(byte_array)

# Using append
my_list.append("Paris")
print("\nUsing append:")
print("Appended List:", my_list)
#my_tuple.append("Pairs")
byte_array.append(4)
print(byte_array)

