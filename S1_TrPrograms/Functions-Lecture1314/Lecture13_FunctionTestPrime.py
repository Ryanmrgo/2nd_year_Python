
def prime(n):
    x=1
    for i in range(2,n):
       if n%i==0:
        x=0
        break
    else:
        x=1
    return x
num=int(input('Enter the number to check'))
result=prime(num)
if result==1:
    print(num, 'is prime')
else:
    print(num,'is not prime' )
'''
def prime(n):
    x=1
    for i in range(2,n):
       if n%i==0:
        x=0
        break
    else:
        x=1
    return x
num=int(input('Enter the number to check'))
i=2
c=1
while True:
    if(prime(i)):
        print('prime no',i)
        c+=1
    i+=1
    if c>=num:
        break
'''



        
