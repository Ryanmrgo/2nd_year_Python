def IsPrime(num):
    x=1
    for i in range(2,num):
        
        if (num%i==0):
            x=0
            break
        else:
            x=1
    return x
num=int(input('How many prime do you want?:'))
i=2
count=1

while True:
    if IsPrime(i):
        print(i,end=',')
        count+=1
    i+=1    
    if count>num:
        break
    
