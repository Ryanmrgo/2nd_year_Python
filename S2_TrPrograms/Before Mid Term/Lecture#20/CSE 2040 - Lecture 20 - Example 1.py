# CSE 2040 - Lecture 20 - Example 1
# Example illustrating types of parameters

# Positional-or-keyword parameters

def create_date(day,month,year):
     return (str(day) + "-" + str(month) + "-" + str(year))

# Calling the function
print()
print("Positional-or-Keyword parameters:")
print("\tDate: " + create_date(4,7,2018))
print("\tDate: " + create_date(2018,7,4))
print("\tDate: " + create_date(year=2018,day=7,month=4))
print("---------------------------------------------------------------------")

