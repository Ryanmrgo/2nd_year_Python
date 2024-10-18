# Python Program to Print Odd Numbers from 1 to N

maximum = int(input(" Please Enter any Maximum Value : "))

for number in range(1, maximum + 1):
    if(number % 2 != 0):
        print("This is odd","{0}".format(number))
    else:
        print("This is even","{0}".format(number))
        
