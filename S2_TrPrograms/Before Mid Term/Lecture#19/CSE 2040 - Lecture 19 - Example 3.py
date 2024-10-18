# CSE 2040 - Lecture 19 - Evarample 3
# Evarample illustrating  nonlocal in Python

# Scope of var - Normal/Local
print()
var = 0
def outer_function():
    var = 1
    def inner_function():
        var = 2
        print("inner_function:", var)

    inner_function()
    print("outer_function:", var)

outer_function()
print("global:", var)
print("----------------------------")
print()

# Scope of var - With nonlocal
var = 0
def outer_function():
    var = 1
    def inner_function():
        nonlocal var
        var = 2
        print("inner_function:", var)

    inner_function()
    print("outer_function:", var)

outer_function()
#inner_function()
print("global:", var)
print("----------------------------")
print()

var = 0
def outer_function():
    var = 1
    def inner_function():
        global var
        var = 2
        print("inner_function:", var)

    inner_function()
    print("outer_function:", var)

outer_function()
print("global:", var)
print("----------------------------")
print()

