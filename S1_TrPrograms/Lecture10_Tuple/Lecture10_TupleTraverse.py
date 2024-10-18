#Lecture 10
#Illustrtion of traversing a tuple
'''
datatuple=(111,[1,'Clara',75.5],(2,'Simon',80.5))
print(' test for datatuple[0]')
print(datatuple[0])
print(' test for datatuple[1][1]')
print(datatuple[1][1])

#Negative indexing
print(' test for datatuple[-1]')
print(datatuple[-1])
'''

#Illustration of Slicing Operator
datatuple=('P','Y','T','H','O','N')
print(datatuple[1:3])
print(datatuple[-2])
print(datatuple[4])


#Changing and updating a tuple
new_tuple=(111,[1,'Clara',75.5],(2,'Simon',80.5))
new_tuple[1][1]='Sharon'
print(new_tuple)


#Deleting a tuple
datatuple1=('P','Y','T','H','O','N')
del(datatuple1)

print(datatuple1)




