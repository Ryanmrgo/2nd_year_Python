'''
elements=[10,20, 0, 40, 15] #this is a list of byte numbers
print(elements)
'''
#x=bytes(elements)#convert the list into byte sequence
x=bytes([10,256, 0])

print(x)

print(id(x))
print(type(x))
#x[0]=50
print(x[0])

