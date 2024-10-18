# Lecture 14 - Example 1

# Counting the digits of an integer
def countDigits(number):
     numberOfDigits = 0;
     temp = abs(number)
     print(temp)
     while (temp != 0):
          numberOfDigits = numberOfDigits +1
          print('count is',numberOfDigits)
          temp = int(temp / 10)
          print('Temp is',temp)
     if (number == 0):
          return 1
     else:
          return numberOfDigits

     
# Main program

# Printing the instructions to the user for input of data
print()
number = int(input("enter input"))
print("The number of digits in " + str(number) + " is " + str(countDigits(number)))
