# CSE 2040 - Lecture 20 - Example 4
# Example illustrating types of parameters

# var-keyword parmeters
def print_total(**elements):
     total = 0
     for key,value in elements.items():
          total = total + value
          print("\t" + str(key) + " - " + str(value))
     print("\n\tTotal is " + str(total) + "\n")  

# Calling the function
print()
print("var-keyword parameters:")
print_total(Jan=31,Feb=28,Mar=31,Apr=30,May=31,June=30)
print_total(Group1=50,Group2=46,Group3=53,Group=63)
print_total(SriLanka=9,India=29,USA=50)
print("---------------------------------------------------------------------")
