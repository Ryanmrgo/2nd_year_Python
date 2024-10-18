'''
mytest1 = 'Today is Monday'
mytest2= 'Today is Monday'

print(id(mytest1))
print(id(mytest2))

print('Test for is operator',mytest1 is mytest2)
print('Test for equal operator',mytest1==mytest2)

number1=10

number2=10
print(id(number1))
print(id(number2))

print('number for is operator',number1 is number2)
print('number for equal operator',number1==number2)

a = [1,2,3]
b = [1,2,3]
#a = (1,2,3)
#b = (1,2,3)
print(id(a))
print(id(b))
print(type(a))
print(type(b))
#c=[1,2,3]

print( a == b)
print(a is b)
#number1=10
'''

a = (1,2,3)
b = (1,2,3)
print(id(a))
print(id(b))

print(type(a))
print(type(b))
#c=[1,2,3]

print( a == b)
print(a is b)




