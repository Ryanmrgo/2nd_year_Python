'''returning a functon'''
def polynomial_generator(a,b,c):
    def polynomial(x):
        return a*x**2+b*x+c
    return polynomial

#function call
poly1 = polynomial_generator(2,3,-1)
poly2 = polynomial_generator(-1,2,1)

print()

print("Polynomial of degree 2 ...")
print(poly1(-2))
print(poly2(-2))
