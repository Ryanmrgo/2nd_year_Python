# Lecture 14 - Example 4

def function1():
     return 1

def function2():
     return None

def function3():
     None

def function4():
     lst = [1] # lst variable is visible only within the function
     lst.append(2)
     lst.append(3)
     lst.append(4)
     return lst

f1 = function1()
f2 = function2()
f3 = function3()
f4 = function4()
print()
# Printing the values returned by the functions
print(f1)

print(f2)
print(f3)

print(f4)
print()

for item in f4:
     print(item)
     
# Printing the values returned by the functions - by calling the functions directly in print
print(function4)
print(function1) # Prints the address of the function

test = False
if (test):
     def function1():
          print("Inside if section")
else:
     def function1():
          print("Inside else section")

print()
#print(function1)





