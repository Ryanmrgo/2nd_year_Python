import datetime

# Understanding how main code executes in Python
print()
globalVar = "August 2018"
print("Current month and year is " + globalVar)

def findMonthNumber(stringVar):
     info = str(datetime.datetime.now())
     print(str(datetime.datetime.now()))
     return info[6:7]

print(findMonthNumber(globalVar))

# Main program section
if __name__ == "__main__":
     print()
     print("I am executed as the main program")
else:
     print("I am importted by another module")
