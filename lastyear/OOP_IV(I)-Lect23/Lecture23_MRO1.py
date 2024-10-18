
#when super classes has constructor
class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)
class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
#access the super class instance vars from c
o=C()
print(C.mro())


class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)
class C(B,A):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
#access the super class instance vars from c
o=C()
print(C.mro())

class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
        super().__init__()
class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)
        super().__init__()
class C(B,A):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
#access the super class instance vars from c
o=C()
print(C.mro())

class A(object):
    def __init__(self):
        self.a='a'
        print(self.a)
        super().__init__()
class B(object):
    def __init__(self):
        self.b='b'
        print(self.b)
        super().__init__()
class C(A,B):
    def __init__(self):
        self.c='c'
        print(self.c)
        super().__init__()
#access the super class instance vars from c
o=C()
print(C.mro())

##another style not using super
class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)

class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)

class C(A, B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        A.__init__(self)  # Call A's __init__
        B.__init__(self)  # Call B's __init__

c_instance = C()
print(C.mro())

    
