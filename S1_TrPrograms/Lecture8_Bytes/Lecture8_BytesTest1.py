#Lecture8-program to understand byte type array
#create a list of byte numbers
elements=[10,20,0,40,15]
#convert the list into bytes type array
x=bytes(elements)

for i in x:
    print(i)
print(id(x))
print(type(x))
#elements[2]=70
#print(elements)
#x[2]=80 #cannot modify the data
print(bytes(0))
print(bytes(1))
print(bytes(4))

