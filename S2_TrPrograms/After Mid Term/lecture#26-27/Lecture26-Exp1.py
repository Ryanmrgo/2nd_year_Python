# Example illustrating anonymous and generator functions
# Anonymous functions
string = lambda a,b,c,d=0 : (str(a) + str(b) + str(c) + str(d))

x = string('A','B','C','D')
y = string(4,3,2,1)
z = string([1,2],[2,3],[3,4])
print()
print(x)
print(y)
print(z)

# Generator functions
'''Generators are functions that return a sequence of values. use yield statement'''
def mygen(x,y):
     while x<=y:
          yield x
          x+=1
g=mygen(5,10)

for i in g:
     print(i,end=' ')


print()
some_sequence = lambda y : (x for x in range(y) if x % 2 == 0)
result = some_sequence(100)
#print(result)
for i in result:
     print(i,end=' ')

