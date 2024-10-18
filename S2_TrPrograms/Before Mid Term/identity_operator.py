first_number=100
second_number=first_number

print ("id(first_number), id(second_number):", id(first_number), id(second_number))
print ("first_number is second_number:", first_number is second_number)
print ("second_number is not first_number:", second_number is not first_number)


#a=[1,2,3]
#b=[1,2,3]
#print ("id(a), id(b):", id(a), id(b))
#print ("a is b:", a is b)
#print ("b is not a:", b is not a)

##print (id(a[0]), id(a[1]), id(a[2]))
##print (id(b[0]), id(b[1]), id(b[2]))

'''The list or tuple contains the memory locations of individual items only
and not the items itself. Hence "a" contains the addresses of 10,20 and 30 integer objects
in a certain location which may be different from that of "b".
Because of two different locations of "a" and "b", the "is" operator returns False
even if the two lists contain same numbers.'''
