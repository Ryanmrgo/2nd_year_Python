#inserting new element into a tuple
names=('Visnu','anupama','Laskmi','Breeshma')
print(names)
lst=[input(('Enter a new name'))]
new=tuple(lst)
pos=int(input('Enter a position'))
names1=names[0:pos-1]
names1=names1+new
names=names1+names[pos-1:]
print(names)
