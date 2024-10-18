# Example illustrating Python decorators 
def outer_function(f):
    def inner_function(x):
        print("\tFunction is " + f.__name__)
        print("\tValue passed is " + str(x))
        #f(x)
    return inner_function

@outer_function
def method1(x):
    print("\tInside method 1!")
@outer_function
def method2(y):
    print("\tInside method 2!")

print()
method1(100)
print()
method2(200)





