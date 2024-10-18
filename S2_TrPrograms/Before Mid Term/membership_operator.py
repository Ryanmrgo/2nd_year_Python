var="Membership Operators"
a="O"
b="ship"
c="in"
d="operators"
print(a,"in",var,":",a in var)
print(b,"not in",var,":",b not in var)
print(c,"in",var,":",c in var)
print(d,"not in",var,":",d not in var)

#finding value in the list 
var = [10,20,30,40]
a = 20
b = 10
c = a-b
d = a/2
print (a, "in", var, ":", a in var)
print (b, "not in", var, ":", b not in var)
print (c, "in", var, ":", c in var)
print (d, "not in", var, ":", d not in var)
#finding value in the Turple 
var = (10,20,30,40)
a = 10
b = 20
print ((a,b), "in", var, ":", (a,b) in var)
var = ((10,20),30,40)
a = 10
b = 20
print ((a,b), "in", var, ":", (a,b) in var)
#finding value in the dictionary 
var = {1:10, 2:20, 3:30}
a = 2
b = 20
print (a, "in", var, ":", a in var)
print (b, "in", var, ":", b in var)
