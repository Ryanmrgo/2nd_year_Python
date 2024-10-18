
l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
      sorted(l, key=lambda x: int(x)))
 
# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:", 
      list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))
 
# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
      list(map(lambda x: str(int(x) + 10), l)))
