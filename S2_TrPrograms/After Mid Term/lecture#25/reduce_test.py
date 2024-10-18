from functools import *

lst=[1,2,3,4,5]
sum=reduce(lambda x, y: x*y, lst)
print(sum)

'''
sum=reduce(lambda a, b: a+b, range(1,5))

print(sum)
'''