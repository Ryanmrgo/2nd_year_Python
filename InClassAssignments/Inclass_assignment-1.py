
byte_seq = bytes([1, 1, 2, 3, 5, 8, 13, 21])
byte_arr = bytearray([1, 1, 2, 3, 5, 8, 13, 21])
my_list = ["Yangon", "Mandalay", "Bangalore", "New York"]
my_tuple = (1, "Jack", 28, 2, "Rob", 30, 3, "Jill", 29)



print("Byte Sequence:", byte_seq)
print("Length:", len(byte_seq))
print("Concatenation:", byte_seq + bytes([34, 55]))
print("Repetition:", byte_seq * 2)
print("Contains 8:", 8 in byte_seq)
print("Not Contains 25:", 25 not in byte_seq)
print("Indexing at position 3:", byte_seq[3])
print("Slicing from 2 to 5:", byte_seq[2:5])



print("\nByte Array:", byte_arr)
print("Length:", len(byte_arr))
print("Concatenation:", byte_arr + bytearray([34, 55]))
print("Repetition:", byte_arr * 2)
print("Contains 8:", 8 in byte_arr)
print("Not Contains 25:", 25 not in byte_arr)
print("Indexing at position 3:", byte_arr[3])
print("Slicing from 2 to 5:", byte_arr[2:5])



print("\nList:", my_list)
print("Length:", len(my_list))
print("Concatenation:", my_list + ["London", "Tokyo"])
print("Repetition:", my_list * 2)
print("Contains 'Yangon':", "Yangon" in my_list)
print("Not Contains 'Paris':", "Paris" not in my_list)
print("Indexing at position 2:", my_list[2])
print("Slicing from 1 to 3:", my_list[1:3])
my_list.append("Dubai")
print("Append:", my_list)
my_list.extend(["Delhi", "Sydney"])
print("Extend:", my_list)



print("\nTuple:", my_tuple)
print("Length:", len(my_tuple))
print("Concatenation:", my_tuple + (4, "John", 32))
print("Repetition:", my_tuple * 2)
print("Contains 'Jack':", "Jack" in my_tuple)
print("Not Contains 40:", 40 not in my_tuple)
print("Indexing at position 5:", my_tuple[5])
print("Slicing from 3 to 7:", my_tuple[3:7])
