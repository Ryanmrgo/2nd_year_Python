#operators in python
'''
https://www.programiz.com/python-programming/operators
'''
#three digit
n = input ("Enter a three-digit number:")
n = int (n)
 
d1 = n% 10
d2 = n% 100 // 10
d3 = n // 100
 
print ("Sum of digits of a number:", d1 + d2 + d3)
'''
#ndigit
n = input ("Enter a three-digit number:")
n = int (n)
sum = 0
while (n != 0): 
       sum = sum + (n % 10)
       n = n//10
print ("Sum of digits of a number:",sum)
'''
#ndigit using function
def getSum(n):
    
    sum = 0
    while (n != 0): 
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum
   
n = 12345
print(getSum(n))
'''
