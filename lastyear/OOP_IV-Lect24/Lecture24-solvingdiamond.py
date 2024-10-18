class A:
    def someMethod(self):
        print("someMethod of A called")

class B(A):
    def someMethod(self):
        print("someMethod of B called")
        super().someMethod()
    
class C(A):
    def someMethod(self):
        print("someMethod of C called")
        super().someMethod()

class D(B,C):
    def someMethod(self):
        print("someMethod of D called")
        super().someMethod()

print()
x = D()
x.someMethod()
print()

