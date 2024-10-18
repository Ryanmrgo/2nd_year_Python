'''
#Calculating time using DECo
import time
def timeit(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("{} took {} seconds to execute".format(func.__name__, end_time - start_time))

    return wrapper
@timeit
def hello():
    time.sleep(2)
    print("Hello, World!")

hello()
'''
#adder function to add numbers
def add_ten(func):
    def wrapper(num1, num2):
        num1, num2 = num1+10, num2+10
        return func(num1, num2)

    return wrapper

@add_ten
def adder(num1, num2):
    return num1 + num2
print(adder(1, 2)) # prints 23

'''

