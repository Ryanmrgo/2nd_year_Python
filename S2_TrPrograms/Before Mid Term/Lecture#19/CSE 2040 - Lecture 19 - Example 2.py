# CSE 2040 - Lecture 19 - Example 2
# Example illustrating  returning from a function

def function1():
     return 1

def function2():
     return None

def function3():
     None

def function4():
     l = [1]
     l.append(2)
     return l
def function5():
     pass

print(function1) # Prints address of the function
print(function2) # Prints address of the function
print(function3) # Prints address of the function
print(function4) # Prints address of the function

x = function1 # Assigns the address of function1 to x
y = x() # Equivalent to calling function1
print(y)

print('Calling Functions and Testing Return Values!')
a=function1()
print(a)
b=function2()
print(b)
c=function3()
print(c)
d=function4()
print(d)

test = True
if test:
     def function1():
          print("Inside if section")
else:
     def function1():
          print("Inside else section")

# Calls function1 defined within the if ... else construct
# As that this the latest address the identifier function1 holds

function1() # Prints "Inside if section"
