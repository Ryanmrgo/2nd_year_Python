a=3

def test():
    a=2
    
    x=globals()['a']
    print("Local:",a)
    print("Copy Global:",x)
    
test()
print("Global:",a)