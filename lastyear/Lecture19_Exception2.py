#example for handling exceptions using try and except
import sys
while True:
    try:
        x=int(input("Enter an integer:"))
        r=1/x
        break
    except:
            print("OOps!:", sys.exc_info()[0],)
            print("please try again")
print()
print("The reciprocal of ",x,"is",r)
