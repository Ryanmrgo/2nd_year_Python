'''
x = b"Bytes objects are immutable sequences of single bytes"
print(x)
print(type(x))



#created from a iterable of ints, string, bytes or buffer objects.
x = bytes('Python,bytes', 'utf8')
print(x)
'''

# create a string using the decode() method of bytes. 
#This method takes an encoding argument, such as UTF-8, and optionally an errors argument.
x = b'El ni\xc3\xb1o come camar\xc3\xb3n'
s = x.decode()

print(type(s))
print(s)
'''
#create a bytes object encoded using 'cp855'
x = b'\xd8\xe1\xb7\xeb\xa8\xe5 \xd2\xb7\xe1'
print(x)
#return a string using decode 'cp855'
y = x.decode('cp855')
print(y)
''''
