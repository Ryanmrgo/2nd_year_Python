#samename for global and local var
a=1
def myfunction():
    a=2
    x=globals()['a']   #Retrieve the value of 'a' using globals()
    print('global var a=',x)
    print('local var a=',a)
myfunction()
print('global var a is',a)
