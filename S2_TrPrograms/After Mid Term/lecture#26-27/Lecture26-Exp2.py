#https://kelvinmwinuka.com/python-higher-order-functions/
#using map fun as a hihger order function
'''
def greet(person):
    #print("Hello, {}!".format(person['age']))
    print("Hello, {}!".format(person['name']))
people = [
    { 'name' : 'Mya Mya', 'age' : 50},
    { 'name' : 'Aye Aye', 'age' : 30},
    { 'name' : 'Ko Ko', 'age' : 28},
    { 'name' : 'Kyaw Kyaw', 'age' : 32},
    { 'name' : 'Kaung Mon', 'age' : 67},
]
#mapObj=list(map(greet, people ))
#print(mapObj)
print(list(map(greet, people )))

'''
#using filter as a higher order function
def legalperson(person):
    return person['age'] >= 25
people = [
    { 'name' : 'Ko Ko', 'age' : 39},
    { 'name' : 'Ma Ma', 'age' : 19},
    { 'name' : 'Mi Mi', 'age' : 27},
    { 'name' : 'Kaung sis', 'age' : 15},
    { 'name' : 'Yun Yun', 'age' : 45},
]
legal_name = list(filter(legalperson, people))
print(legal_name)
print(list(filter(legalperson, people)))


