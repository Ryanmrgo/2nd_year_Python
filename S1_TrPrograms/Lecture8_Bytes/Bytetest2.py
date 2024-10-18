
# simple list of integers
list = [1, 2, 3, 4]
 
# iterable as source
array = bytearray(list)
array[0]=253
 
print(array)
print("Count of bytes:", len(array))
