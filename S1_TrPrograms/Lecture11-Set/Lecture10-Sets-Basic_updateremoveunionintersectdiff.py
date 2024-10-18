#Lecture10-updating a set in python
#add,update
dataset1={10,20,30,40,50}
print(dataset1)
dataset1.add(35)
print('adding',dataset1)
dataset1.update([5,18,27])
print('updating',dataset1)
#discard,remove,pop
dataset11={10,20,30,40,50,60}
print(dataset11)
dataset11.discard(50)
print('discard1',dataset11)
dataset11.discard(35)
dataset11.discard(30)
print('discard2',dataset11)
dataset11.remove(60)
print('remove',dataset11)
dataset11={10,20,30,40,50,60,70}
dataset11.pop()
print(dataset11)
#set Union
x={10,20,30}
y={30,40,50,60}
print(x|y)
print(x.union(y))
print(y.union(x))
#Set Intersection
x={10,20,30}
y={30,20,50,60}
print('intersection1',x&y)
print(x.intersection(y))
print(y.intersection(x))
#Set Difference
x={10,20,30}
y={30,40}
print(x-y)
print(x.difference(y))
print(y-x)
print(y.difference(x))
#Set Symmetric Difference
x={10,20,30}
y={30,40}
print(x^y)
print(x.symmetric_difference(y))
print(y^x)
print(y.symmetric_difference(x))
#in in set 
x={10,20,30}
y={30,40}
print(10 in x)
print(50 in y)



























