'''A decorator to increase the value of a function by 2 '''
'''
def decor(fun):
    def inner():
        value = fun()
        return value+2
    return inner

#take a function to which decorator should be applied
def num():
    return 10

#call decorator function and pass num
result_fun = decor(num)  #result_fun represents 'inner' function
print(result_fun())      #call the result_fun and display the result
'''
'''A python program to apply a decorator to a function using @ symbol'''

def decor(fun):
    def inner():
        value = fun()
        return value+2
    return inner
    
@decor
def num():
    return 10

#call the num() function and display the result
print(num())

'''A python program to create two decorators.'''
def decor(fun):
    def inner():
        value = fun()
        return value+2
    return inner

def decor1(fun):
    def inner():
        value = fun()
        return value*2
    return inner

def num():
    return 10

result_fun = decor(decor1(num))
print(result_fun())

'''To apply two decorators to the same function using @ symbol'''
def decor(fun):
    def inner():
        value = fun()
        return value+2
    return inner

def decor1(fun):
    def inner():
        value = fun()
        return value*2
    return inner

@decor
@decor1
def num():
    return 10

print(num())
