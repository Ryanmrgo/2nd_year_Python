# Lecture 13- Example 1

def compute(a, b, c = 1):
     ''' Function having two mandatory and one default parameter '''
     return a ** 2 + b ** 2 - c

a = 3
b = 2
c = 5
#print(compute(a,b,c))

# Main

#print(compute(1, 2))               # returns 4 - positional and default

#print(compute(1, 2, 3))            # returns 2 - only positional

#print(compute(c = 5, b = 2, a = 3)) # returns 8 - only named

#print(compute(b = 2, a = 2))       # returns 7 - named and default

#print(compute(5, c = 2, b = 1))    # returns 24 - positional and named

print(compute(8, b = 0))           # returns 63 - positional, named and default


print()
#print(compute(c = c, b = b, a = a)) 
