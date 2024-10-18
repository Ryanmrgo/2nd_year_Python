#lecture10

#To check the list type
roll_numbers = ["CSE-001","CSE-002","CSE-003","CSE-004"]
print('Test list is')
print(type(roll_numbers))


#illustration of list functions.
datalist=[23,45,31,53,62]
print( 'len test is')
print(len(datalist))
print( 'max test is')
print(max(datalist))
print( 'min test is')
print(min(datalist))


'''
#illustration of list comprehension
even=[i for i in range(50) if i%2==0]
print(even)
odd=[i for i in range(50) if i%2!=0]
print(odd)
'''

#List membership,illustration of membership test
datalist=[11,22,33,44,55]
print(11 in datalist)
print(66 not in datalist)

'''
#illustration of iterating throug list
for city in ['Mandalay','Yangon', 'Sagaing']:
    print("I visted",city)
'''

