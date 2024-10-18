def find_fac(n):
    prod=1
    while n>=1:
      prod=prod*n
      n=n-1

    return prod
'''  
#factorial of one number
num=int(input("Enter a number to find factorial:"))

fact=find_fac(num)
print("The factorial number of {} is {}.".format(num,fact))
'''
'''
#factorial of 1 to num
for i in range(1,11):
 print("The factorial number of {} is {}.".format(i,find_fac(i)))

'''