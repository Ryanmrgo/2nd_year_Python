x = "hello"
#x=5

if not type(x) is int:
  raise TypeError("Only integers are allowed")

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") 


