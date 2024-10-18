'''pass integer to a function and modify it'''
'''
def modify(x):
    x=15
    print(x,id(x))

x=10
modify(x)
print(x,id(x))
'''

'''pass a list to function and modify it'''
'''
def modify(lst):
    #lst.append(9)  #modify list
    print(lst)

lst=[1,3,6]
modify(lst)
print(lst)
'''
'''pass a function as parameter to another function'''
'''
def display(fun):
    return 'Hai'+fun

def message():
    return 'How are you'

print(display(message))
'''
'''a function can return another function'''
def display():
    def message():
        return 'How are you'
    return message

fun=display()
print(fun())
