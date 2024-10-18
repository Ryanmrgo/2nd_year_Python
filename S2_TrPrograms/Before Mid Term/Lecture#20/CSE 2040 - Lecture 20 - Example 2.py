# CSE 2040 - Lecture 20 - Example 2
# Example illustrating types of parameters

# Positional-or-keyword parameters
def create_time(hour=0,minutes=0,seconds=0):
     return (str(hour) + ":" + str(minutes) + ":" + str(seconds))

# Calling the function
print()
print("Keyword-only parameters:")
print("\tTime: " + create_time(2,12,45)) #follow order of arguments

print("\tTime: " + create_time(seconds=45,minutes=12,hour=2))
print("---------------------------------------------------------------------")

