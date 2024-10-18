
#sys.intern() to intern strings for performance.
#This function allows you to compare their memory addresses rather than comparing the strings character-by-characte


from sys import intern
mytest1 = 'Today is Monday'
mytest2= 'Today is Monday'

print(id(mytest1))
print(id(mytest2))

#print(mytest1 is mytest2)

print(mytest1==mytest2)
'''
print(type(mytest1))
print(type(mytest2))
mytest3='Today is Tuesday'
print(mytest1 is mytest3)
print(mytest1 == mytest3)

#print(intern(mytest1) is intern(mytest2))
'''
'''

number1=10
number2=10
print(id(number1))
print(id(number2))
print(number1 is number2)
print(number1==number2)


number3=257
number4=257
print(id(number3))
print(id(number4))
print(number3 is number4)
print(number3==number4)

'''


a = [1, 2, 3]
b = a.copy()
print(id(a))
print(id(b))
print(type(a))
print(type(b))
print( a == b)
print(a is b)

c=3
a=3
b=a

d=3
print(id(c))
print(id(d))
print(c is d)
print(c==d)


a = [1,2,3]
b = [1,2,3]
c=[1,2,3]
print(id(a))
print(id(b))
print( a == b)
print(a is b)
#a=[1,4,5]
#print(id(a))
'''






