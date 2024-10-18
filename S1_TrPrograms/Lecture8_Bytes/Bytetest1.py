'''
#this method return a single character based on the integer value.
x = chr(60)
print(x)
x = chr(50)
print(x)
#2
#create a list with integers in the range 0 through 255
y = [70, 111, 106, 94, 101, 100, 22, 95, 105, 22, 91, 87, 125, 135]
print(y)
[70, 111, 106, 94, 101, 100, 22, 95, 105, 22, 91, 87, 125, 135]
#create a bytes object from a list of integers in the range 0 through 255.
z = bytes(y)
print(z)
b'Foj^ed\x16_i\x16[W}\x87'
'''

# Creates bytearray from byte literal
arr1 = bytearray(b"abcd")
 
# iterating the value
for value in arr1:
    print(value)
     
# Create a bytearray object
arr2 = bytearray(b"aaaacccc")
 
# count bytes from the buffer
print("Count of c is:", arr2.count(b"c"))
