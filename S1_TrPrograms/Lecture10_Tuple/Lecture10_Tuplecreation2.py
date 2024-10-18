#Lecture 10
#tuple one as a string
empty_tuple=()
print(empty_tuple)
print('test empty',type(empty_tuple))

#tuple1=("a")# declare as tuple but work as a string
tuple1=("a",)
print('Test tuple1',tuple1)
print('Test tuple',type(tuple1))


tuple11=("a",)# put comma now work as a tuple
print('Test tuple11',type(tuple11))


tuple2=("a","b")
tuple3=("a","b","c")
tuple4="a","b","c"
print(tuple2)
print(type(tuple2))
print(tuple3)
print(tuple4)
print(type(tuple4))



#declare tuple,no need patherenthesis
tuple1=1
print(type(tuple1))
tuple11=1,
tuple2=1,2,3
tuple3=1,2,3,4
print(type(tuple1))
print(type(tuple11))
print(type(tuple2))
print(type(tuple3))

#illustration of declaring a tuple
t=(7,'python',2+8j)
print(type(t))
print(t[1])

#print('tuple11',t[0]=8)

datatuple=(111,[],(2,"Simon",80.5))#Nested tuple
print(type(datatuple))
print(datatuple[0])
print(datatuple[1])
print(datatuple[2])

print(datatuple[2][1])

