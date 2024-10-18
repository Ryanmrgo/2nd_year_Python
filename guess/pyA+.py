
     #Write a program to print the given number is odd or even.
        
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
       print("{0} is Even".format(num))
    else:
       print("{0} is Odd".format(num))
#############################################################################################
    #Write a program to find the given number is positive or negative.
        
    num = float(input("Enter a number: "))
    # Input: 1.2
    if num > 0:
       print("Positive number")
    elif num == 0:
       print("Zero")
    else:
       print("Negative number")
    #output: Positive number
#############################################################################################
    #Write a program to find the sum of two numbers.
        
    num1 = int(input("Enter Number1: "))
    # Input1 : 21
    num2 = int(input("Enter Number2: "))
    #  Input2 : 11
    print("sum of given numbers is:", num1 + num2)
    #  Output2 : 32 
#############################################################################################
    #Write a program to find if the given number is prime or not.
        
    num = int(input("enter a number: "))
    # input: 23
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
    # 23 is a prime number
#############################################################################################
    #Write a program to check if the given number is palindrome or not.
        
    num = int(input("Enter a number: "))
    # Input: 12321
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
      print('Palindrome')
    else:
      print("Not Palindrome")
    # Output: Palindrome
#############################################################################################
    #Write a program to check if the given number is Armstrong or not.
        
    num = int(input("Enter a number: "))
    # Input: 407
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")
    # Output: 407 is an Armstrong number
#############################################################################################
    #Write a program to check if the given strings are anagram or not.
        
    def check(s1, s2):
        
        if(sorted(s1)== sorted(s2)):
            print("The strings are anagrams.")
        else:
            print("The strings aren't anagrams.")        
            
    s1 = input("Enter string1: ")
    # input1: "listen"
    s2 = input("Enter string2: ")
    # input2: "silent"
    check(s1, s2)
    # Output: the strings are anagrams.
#############################################################################################
    #Write a program to find a maximum of two numbers.
        
    def maximum(a, b):
        
        if a >= b:
            return a
        else:
            return b
        
    a = int(input("Enter a number: "))
    # input1: 2
    b = int(input("Enter a number: "))
    # input2: 4
    print(maximum(a, b))
    # output: 4
#############################################################################################
    #Write a program to find a minimum of two numbers.
        
    def minimum(a, b):
        
        if a <= b:
            return a
        else:
            return b
        
    a = int(input("Enter a number: "))
    # input1: 2
    b = int(input("Enter a number: "))
    # input2: 4
    print(minimum(a, b))
    # output: 2
#############################################################################################
    #Write a program to find a maximum of three numbers.
        
    def maximum(a, b, c):
        if (a >= b) and (a >= c):
            largest = a
        elif (b >= a) and (b >= c):
            largest = b
        else:
            largest = c
            
        return largest
    a = int(input("Enter a number: "))
    # Input1: 10
    b = int(input("Enter a number: "))
    # Input2: 14
    c = int(input("Enter a number: "))
    # Input3: 12
    print(maximum(a, b, c))
    # Output: 14
#############################################################################################
    #Write a program to find a minimum of three numbers.
        
    a = int(input('Enter first number  : '))
    # 12
    b = int(input('Enter second number : '))
    # 14
    c = int(input('Enter third number  : '))
    # 11
    smallest = 0
    if a < b and a < c :
        smallest = a
    if b < a and b < c :
        smallest = b
    if c < a and c < b :
        smallest = c
    print(smallest, "is the smallest of three numbers.")
    # 11 is the smallest of three numbers.
#############################################################################################
    #Write a program to find a factorial of a number.
        
    num = int(input("Enter a number: "))
    # 7
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print("The factorial of",num,"is",factorial)
       # 5040
#############################################################################################
    #Write a program to find a fibonacci of a number.
        
    nterms = int(input("How many terms? "))
    # 7
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
    # Fibonacci sequence:
    # 0
    # 1
    # 1
    # 2
    # 3
    # 5
    # 8
#############################################################################################
    #Write a program to find GCD of two numbers.
        
    def gcd(a, b):
        if (a == 0):
            return b
        if (b == 0):
            return a
        if (a == b):
            return a
        if (a > b):
            return gcd(a-b, b)
        return gcd(a, b-a)
    a = 98
    b = 56
    if(gcd(a, b)):
        print('GCD of', a, 'and', b, 'is', gcd(a, b))
    else:
        print('not found')
#############################################################################################
    #Write a program to print the following pattern.

# *
# * *
# * * *
# * * * *
# * * * * *   
def myfunc(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")
n = 5
myfunc(n)
#############################################################################################
    #Write a program to print the following pattern.
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

def myfunc(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = 5
myfunc(n)
#############################################################################################
    #Write a program to print the following pattern.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5   
    

def num(n):
    num = 1
    for i in range(0, n):
        num = 1
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5
num(n)
#############################################################################################
    #Write a program to print the following pattern.
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
  

def num(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")
n = 5
num(n)
#############################################################################################
    #Write a program to print the following pattern.
# A 
# B B
# C C C
# D D D D
# E E E E E
    

def alphapat(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
    
        print("\r")
n = 5
alphapat(n)
#############################################################################################
    #Write a program to print the following pattern.

  
# A 
# B C
# D E F
# G H I J
# K L M N O
def contalpha(n):
    num = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print()
n = 5
contalpha(n)
