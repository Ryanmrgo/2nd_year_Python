#illustration of creating and Accessing a dictionary
'''
data_dict2={'Name':'Robin','Rollno':'111'}
print(data_dict2)
#illustration of updating a dictionary
data_dict2['Rollno']=121
data_dict2['Name']='Cynthia'
print(data_dict2.get('Name'))
print(data_dict2.get('Rollno'))


#Illustration of removing or deleting a dicitionary elements
data_dict={'Name':'Robin','Rollno':'111','Marks':[40,50,60],'Mobileno':9764377641}
print('my test now',data_dict)

#giving key return value
print('pop test',data_dict.pop('Rollno'))


#printing key value Pair
print('popitem test',data_dict.popitem())

del data_dict['Marks']
print('ny test for del is',data_dict)


print('delettest',data_dict)
print(data_dict.clear())


# random sales dictionary(Test items())
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print('my sale item 1',sales.items())
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
items = sales.items()
print('Original items:', items)


# delete an item from dictionary
del[sales['apple']]
print('Updated items:', items)
'''
'''

#Test keys(),return dictionary keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)
'''
'''
#Dictionary update method
# Dictionary with three items  
Dictionary1 = { 'A': 'Geeks', 'B': 'For', } 
Dictionary2 = { 'B': 'Geeks' } 
  
# Dictionary before Updation 
print("Original Dictionary:") 
print(Dictionary1) 
  
# update the value of key 'B' 
Dictionary1.update(Dictionary2) 
print("Dictionary after updation:") 
print('updated dictionary',Dictionary1)
'''
#update
d = {'x': 2}

d.update(y = 3, z = 0)
print(d)


#dictionary copy mehtod
original = {1:'one', 2:'two'}
new = original.copy()

print('Orignal: ', original)
print('New: copy dictionary ', new)






            

