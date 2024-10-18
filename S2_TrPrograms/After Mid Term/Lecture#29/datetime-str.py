'''datetime is a built-in module in Python for working with dates and times.
datetime is both a module and a class within that module.
When you import datetime like this,you're specifically
importing the datetime class from the datetime module.
The datetime class allows you to create objects
that represent specific points in time (dates and times).'''

'''
from datetime import datetime

print(repr(datetime.now()))  
print(str(datetime.now()))   
'''

import datetime
mydate = datetime.datetime.now()
print("__str__() string:",mydate.__str__())
print("str() string:", str(mydate))

print("__repr__() string: ", mydate.__repr__())
print("repr() string: ", repr(mydate))

