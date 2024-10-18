# Lecture 14 - Example 3

# Using optional parameters

def dayToday(day="I don't know", date="Unknown"):
     ''' Function using day as an optional parameter '''
     print('Today is ' + day + " and date is " + date)

# Calling dayToday function
print("-------------------------------------------------------")
#dayToday('Sunday')
#dayToday() # No argument, hence the default value is printed

#print("-------------------------------------------------------")
#dayToday(date="15 Jan 2024", day="Monday")
dayToday("30 Jan 2022", "Sunday")
