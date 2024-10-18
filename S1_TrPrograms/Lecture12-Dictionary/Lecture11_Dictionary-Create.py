#illustration of creating a dictionary
'''
data_dict1={'Name':'Robin','Rollno':'111'}
print(data_dict1)

data_dict2={'Name':'Robin','Rollno':'111','Marks':[45,67,74]}
print(data_dict2)
data_dict3={'Name':'SAM','Rollno':'222','Marks':[70,47,74]}
print(data_dict3)
data_dict4={'Name':'Karl','Rollno':'333','Marks':[45,87,71]}
print(data_dict4)
print(data_dict1.get('Name'))
print(data_dict1.get('Rollno'))
print(data_dict1.get('Marks'))
print(data_dict3.get('Name'))
print(data_dict3.get('Rollno'))
print(data_dict3.get('Marks'))


#loop in dict
room_num = {'john': 425, 'tom': 212, 'isaac': 345}
for k, v in room_num.items():
    print (k + ' is in room ' + str(v))
 '''   

#nested dictioary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)


## Accessing nested
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])


##changing and addding element in nested
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'
print(people[3])
print(people)


            

