
def mygen(a,b):
    while a<=b:
        yield a
        a+=1
        
g=mygen(5,10)

for i in g:
	print(i,end=" ")
