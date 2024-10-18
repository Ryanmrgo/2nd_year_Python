# CSE 3040 - Lecture 9 - Example 1
# Example illustrating use of core type bytes, bytearray and str

# Using bytes, bytearray and str

print()
print()
# Using bytes - Immutable type
byte_seq = bytes([101,102,103,104,105])
print("First element of byte_seq: " + str(byte_seq[0]))
#byte_seq[0]=110
print()

# Using bytearray - Mutable type
byte_arr = bytearray([41,42,43,44,45])
print("First element of byte_arr: " + str(byte_arr[0]))
#byte_arr[0]=110
#print("After changing First element of byte_arr: " + str(byte_arr[0]))
print()

# Using string - Immutable type
string = "101,102,103,104,104"
print("First element of string: " + string[0])
#string[0] = "X"
print()

'''
# Printing the values in full
print("Printing byte_seq: " + str(byte_seq))
print("Printing byte_arr: " + str(byte_arr))
print("Printing string: " + str(string))
print()


# Bytes, Byte array, and string can be pointed to a new byte sequence, new byte array and a new string
byte_seq = bytes([61,62,63,64,65,66,67,68,69,70])
byte_arr = bytearray([40,50,60,70,80])
string = "Hello world"

# Printing the values in full, to understand the changed values
print("Printing byte_seq (changed): " + str(byte_seq))
print("Printing byte_arr (changed): " + str(byte_arr))
print("Printing string (changed): " + str(string))
print()
'''

