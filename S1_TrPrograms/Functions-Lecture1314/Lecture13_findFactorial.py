#to find factiorial
def fact (n):
    prod=1
    while n>=1:
        prod*=n
        n-=1
    return prod
for i in range (1,6):
    print('Factorial of {} is {}'.format(i,fact(i)))
