# CSE 2040 - Lecture 19 - Example 5
# Example illustrating types of parameters

# Combining: Position+var-keywords
def print_total(what,**elements):
     total = 0
     print(what)
     for key,value in elements.items():
          total = total + value
          print("\t" + str(key) + " - " + str(value))
     print("\n\tTotal is " + str(total) + "\n")  

# Calling the function
print()
print("Combining:")
print_total("Months",Jan=31,Feb=28,Mar=31,Apr=30,May=31,June=30)
print_total("Groups",Group1=50,Group2=46,Group3=53,Group=63)
print_total("States of countries",SriLanka=9,India=29,USA=50)
print("---------------------------------------------------------------------")
