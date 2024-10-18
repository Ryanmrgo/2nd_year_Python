import sys
#list examples
'''
prime_numbers=[2,3,5,7,11,13,17]
#Tuple examples
perfect_squares=(1,4,9,16,25,36)
print("List Methods")
print(dir(prime_numbers))

print(80*" -")
print("tuple Methods")
print(dir(perfect_squares))


#to check list and tuple size
print(dir(sys))
print(help(sys.getsizeof))
list_eg=[1,2,3,'a','b','c',True,3.14159]
tuple_eg=(1,2,3,'a','b','c',True,3.14159)
print("list size",sys.getsizeof(list_eg))
print("tuple size",sys.getsizeof(tuple_eg))
'''

#To check performance
import timeit
list_test=timeit.timeit(stmt="[1,2,3,4,5]" , number=1000000)
#list_test=  timeit.timeit(stmt='[1,2,3,4,5]', setup='pass', timer='pass', number=1000000, globals=None)
tuple_test=timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)
print('list time',list_test)
print('tuple time',tuple_test)

