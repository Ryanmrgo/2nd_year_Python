#illustration of creating a tuple
#homogeneous data element
'''
new_tuple=(1,2,3,4)
print(type(new_tuple))
print(new_tuple)

#heterogeneous data element
new_tuple1=(1,"John",55.5)
print(new_tuple1)


#heterogeneous and nested data element
new_tuple2=(111,[1,"Clara",75.5],(2,"Simon",80.5))
print(type(new_tuple2))
print(new_tuple2)
new_tuple2[1][0]=9000
#new_tuple2[2][1]='Book'
'''
#Unpacking Tuple
#Illustration of unpacking a tuple
new_tuple2=(111,[1,"Clara",75.5],(2,"Simon",80.5))
x,y,z=new_tuple2
print(x)
print(y)
print(z)

