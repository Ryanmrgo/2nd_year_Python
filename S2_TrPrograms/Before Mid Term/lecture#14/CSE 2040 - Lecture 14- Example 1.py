# CSE 2040 - Lecture 14 - Example 1
# Example illustrating different combinations of slicing operator

# Using list
country_list = ["Thailand","China","Indonesia","Sri Lanka",\
                "Bangladesh","Myanmar","India"]

for i in range(len(country_list)):
     print(country_list[i])

begin = 0
end = len(country_list)

# [begin: end]
print(country_list[begin:end])

# [begin: end: step]
print(country_list[begin:end:2])

# [begin:]
print(country_list[begin:])

# [:end]
print(country_list[:end])

# [::step]
print(country_list[::3])

# [begin: -end]
print(country_list[begin:-end]) # Using negative index results in null list

# [-end:begin]
print(country_list[-end:begin]) # Using negative index results in null list

