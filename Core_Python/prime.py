def IsPrime(num):
    x=1
    for i in range(2,num):
        
        if (num%i==0):
            x=0
            break
        else:
            x=1
    return x

n=int(input('Enter a number to check prime or not:'))
           
result=IsPrime(n)
if result==1:
    print("{} is a prime number.".format(n))
else:
    print("{} is a not prime number.".format(n))


        
    