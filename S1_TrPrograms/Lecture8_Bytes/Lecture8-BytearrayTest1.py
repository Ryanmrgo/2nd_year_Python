 #create a bytearray from a bytes object
x = bytearray(b"Python Bytes")
print(x)
#bytearray(b'Python Bytes')
#create a bytearray from a string defining the standard of coding
x = bytearray("Python Bytes", "utf8")
print(x)
bytearray(b'Python Bytes')
#create a bytearray from a list of integers in the range 0 through 255
x = bytearray([94, 91, 101, 125, 111, 35, 120, 101, 115, 101, 200])
print(x)
#bytearray(b'^[e}o#xese\xc8')
print(x[0])
