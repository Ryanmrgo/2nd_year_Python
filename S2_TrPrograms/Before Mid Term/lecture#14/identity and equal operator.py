'''
sys.intern() to intern strings,String literals are inherently interned
This function allows you to compare their memory addresses rather than comparing the strings character-by-characte
'''
'''
##from sys import intern
mytest1 = 'Today is Monday'
mytest2= 'Today is Monday'
print(id(mytest1))
print(id(mytest2))
print(mytest1 is mytest2)
print(mytest1==mytest2)
print(type(mytest1))
print(type(mytest2))
mytest3='Today is Tuesday'
print(mytest1 is mytest3)
print(mytest1 == mytest3)

number1=10
number2=10
print(id(number1))
print(id(number2))
print(number1 is number2)
print(number1==number2)

a = [1, 2, 3]
b = a.copy()
c=a
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))
print(type(a))
print(type(b))
print(type(c))
print( a == b)
print(a is b)
print( a == c)
print( a is c)

c=3
a=3
#b=a.copy() #'int' object has no attribute 'copy'
b=a
d=3
print(id(c))
print(id(d))
print(c is d)
print(c==d)
print(id(a))
print(id(b))
print(a is b)
print(a==b)

##the lists are distinct objects,
#the memory addresses of individual elements in the lists are same
a = [1,2,3]
b = [1,2,3]
c = [1,2,3]
print(id(a))
print(id(b))
print(id(c))
print( a == b)
print(a is b)
print (id(a[0]), id(a[1]), id(a[2]))
print (id(b[0]), id(b[1]), id(b[2]))

'''





