from sys import intern
mytest1 = 'Today is Monday'
mytest2='Today is Monday'
print(type(mytest1))
print(type(mytest2))
mytest3='Today is Tuesday'
print(mytest1 is mytest2)

print(mytest1 == mytest2)

print(id(mytest1) is id(mytest2))

