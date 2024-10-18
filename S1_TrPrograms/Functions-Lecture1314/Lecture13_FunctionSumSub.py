def sub(a,b):
    #c=a+b
    d=a-b
    return d
y=sum_sub(10,5)
#print('Result of Addition',x)
print('Result of Subtraction',y)

def sum(a,b):
    c=a+b
    #d=a-b
    return c
x=sum(10,5)
print('Result of Addition',x)
#print('Result of Subtraction',y)


#Returning Multiple Values form a function
def sum_sub(a,b):
    c=a+b
    d=a-b
    return c,d
x,y=sum_sub(10,5)
print('Result of Addition',x)
print('Result of Subtraction',y)

