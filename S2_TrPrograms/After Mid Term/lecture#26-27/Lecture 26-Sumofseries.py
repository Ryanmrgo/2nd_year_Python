# Python Decorators - DECORATOR WITH var-pos PARAMETERS
def what_series(*args):
     def decorator_sum(function):
          def sum_it(n):
               ''' Higher order function that will sum any series '''               # Printing the message about the series
               print('Sum of the series - ',end=' ')
               length = len(args)
               for i in range(length):
                    print(args[i],end=' ')
                    print("+",end=' ')
               print("...")
               sum = 0
               ith = 1
               while ith <= n:
                    sum = sum + function(ith)
                    ith = ith + 1
               return sum
          return sum_it
     return decorator_sum

a = 1
b = 2
@ what_series(a,b,3,4) # Passing both variables and arguments
def naturalTerm(x):
        return x

@ what_series("1^3","2^3","3^3","4^3")
def cubeTerm(x):
        return x * x * x; 

@ what_series("1/1","1/2","1/3","1/4")
def series1Term(x):
        return 1/x

n = 10
print()
print(naturalTerm(10))
print()
print(cubeTerm(4))
print()
print(series1Term(3))
print()


