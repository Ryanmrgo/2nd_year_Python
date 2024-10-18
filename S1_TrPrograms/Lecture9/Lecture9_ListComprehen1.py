def square(x):
    return x*x;
fun_test=[square(x) for x in range(1,11)]
print(fun_test)
# Add two list

a=[1,2,3,4]
b=[10,1,6]
c=[1,2,3,4]
samelen_add=[a[i]+c[i] for i in range(0,len(a))]
print(samelen_add)

add_list=[x for x in a for y in b]
add_list1=[x+y for x in a for y in b]
#print(add_list)
print(add_list1)

