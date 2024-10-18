'''
# array of size 0 will be created
 
# iterable as source
array = bytearray()
 
print(array)
'''
import codecs
#Define the original bytearray
test_list = [124, 67, 45, 11]
byte_array = bytearray(test_list)
 
#Convert bytearray to hexadecimal string using codecs.encode()
#hex_string = codecs.encode(byte_array, 'hex').decode()
hex_string = str(codecs.encode(byte_array, 'hex'))

#hex_string = codecs.encode(byte_array, 'hex').decode()

 
#Print the result
print("The string before conversion: " + str(test_list))
print("The string after conversion: " + hex_string)
for i in hex_string:
      print(ord(i),end=" ")

'''
# initializing list
test_list = [124, 67, 45, 11]
 
# printing original list
print("The original string is : " + str(test_list))
 
# using join() + format()
# Converting bytearray to hexadecimal string
res = ''.join(format(x, '02x') for x in test_list)
 
# printing result
print("The string after conversion : " + str(res))
'''
'''
import binascii
 
# initializing list
test_list = [124, 67, 45, 11]
 
# printing original list
print("The original string is : " + str(test_list))
 
# using binascii.hexlify()
# Converting bytearray to hexadecimal string
res = binascii.hexlify(bytearray(test_list))
 
# printing result
print("The string after conversion : " + str(res))
'''
'''
# define the original bytearray
test_list = [124, 67, 45, 11] 
byte_array = bytearray(test_list)
 
print("The string before conversion: " + str(test_list))
# convert bytearray to hexadecimal string
hex_string = byte_array.hex()
 
# print the result
print("The string after conversion: " + hex_string)
'''

