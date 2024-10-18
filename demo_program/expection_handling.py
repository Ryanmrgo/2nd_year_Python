a = 5
b = 0

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number:"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero" , e)

except ValueError as e:
    print("Invalid Input")#out put this exception when the user input is non_integer

except Exception as e:
    print("Something went Wrong...")

finally:
    print("resource Closed")
