#same name for global and local variables
a=1#this is global var
def myfunction():
    a=2 #this is local var
    print('Local a value is',a)
myfunction()
print('Global a value is',a)#display global var
