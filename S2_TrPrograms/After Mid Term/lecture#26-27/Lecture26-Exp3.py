def hello_decorator(func):
    def wrapper():
        print('Before calling func')
        func()
        print('After calling func')
    return wrapper
def hello():
    print('Hello, World!')

decorated_hello = hello_decorator(hello)
decorated_hello()
'''
def hello_decorator(func):
    def wrapper():
        print('Before calling func')
        func()
        print('After calling func')
    return wrapper
@hello_decorator
def hello():
    print('Hello, World!')
hello()
'''
