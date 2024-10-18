def Find_Fact_Prime(n,num):
    prod=1
    while n>=1:
      prod=prod*n
      n=n-1
      
    x=1
    for i in range(2,num):
        
        if (num%i==0):
            x=0
            break
        else:
            x=1

    result=x
    if result==1:
     print("{} is a prime number.".format(n))
    else:
     print("{} is a not prime number.".format(n))
    return prod
   
Find_Fact_Prime(n=3,num=7)
  

print("Result for factorial 7 is:",Find_Fact_Prime())
print("Result for factorial 7 is:",Find_Fact_Prime())
