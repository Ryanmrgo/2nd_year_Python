# CSE 3040 - Lecture 9 - Example 2
# Example illustrating use of common functions

# Using bytes, bytearray and str

print()
print()
# Using bytes - Immutable type
byte_seq = bytes([101,102,103,104,105])
print("First element of byte_seq: " + str(byte_seq[0]))
print()

# Using bytearray - Mutable type
byte_arr = bytearray([41,42,43,44,45])
print("First element of byte_arr: " + str(byte_arr[0]))
print()

# Using string - Immutable type
string = "101,102,103,104,104"
print("First element of string: " + string[0])
print()

print(len(byte_seq))
print(len(byte_arr))
print(len(string))
#using slicing method
print(byte_seq[slice(1,3)]) 
print(byte_arr[slice(1,3)])
#using full colon notation for slicing
print(byte_arr[1:3])
print(string[1:3])

'''Length – len(var)
Concatenation – '+' operator
Repetition – '*' operator
Indexing – using value between 0 to len(var) - 1
Slicing – using two indices within square brackets, separated by a colon
'''
