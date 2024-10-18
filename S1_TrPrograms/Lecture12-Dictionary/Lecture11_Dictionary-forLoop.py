#illustration of using for loop with dictionary
#'''
'''
data_dict={'Name':'Robin','Rollno':111,'Marks':[40,50,60],'Mobile':'09786467476'}
for i in data_dict:
    print(data_dict[i])
#'''

 '''  
#illustration of membership test
data_dict={'Name':'Robin','Rollno':111,'Marks':[40,50,60],'Mobile':'09786467476'}
print('Name' in data_dict)
print('Robin' in data_dict)



'''
#using set to find the missing key
# Python code to find the difference in 
# keys in two dictionary 
# Initialising dictionary  
dict1= {'key1':'Geeks', 'key2':'For', 'key3':'geeks'} 
dict2= {'key1':'Geeks', 'key2:':'Portal'}  
diff = set(dict2) - set(dict1)  
# Printing difference in 
# keys in two dictionary 
print(diff)
'''
'''
#Using dict comprehesion
# Python code to demonstrate 
# intersection of two dictionaries  
# using dict comprehension 
# inititialising dictionary 
ini_dict1 = {'nikhil': 1, 'vashu' : 5,  
             'manjeet' : 10, 'akshat' : 15} 
ini_dict2 = {'akshat' :15, 'nikhil' : 1, 'me' : 56} 
  
# printing initial json 
print ("initial 1st dictionary", ini_dict1) 
print ("initial 2nd dictionary", ini_dict2#intersecting two dictionaries 
final_dict = {x:ini_dict1[x] for x in ini_dict1  
                              if x in ini_dict2} 
# printing final result 
print ("final dictionary", str(final_dict))
'''
'''       
### combining two dictionary

# Python code to demonstrate combining  
# two dictionaries having same key 
  
# initialising dictionaries 
ini_dictionary1 = {'nikhil': 1, 'akash' : 5,  
              'manjeet' : 10, 'akshat' : 15} 
ini_dictionary2 = {'akash' : 7, 'akshat' : 5,  
                                    'm' : 15} 
  
# printing initial dictionaries 
print ("initial 1st dictionary", str(ini_dictionary1)) 
print ("initial 2nd dictionary", str(ini_dictionary2)) 
  
# combining dictionaries 
# using dict comprehension and set 
final_dictionary =  {x: ini_dictionary1.get(x, 0) + ini_dictionary2.get(x, 0) 
                    for x in set(ini_dictionary1).union(ini_dictionary2)} 
  
# printing final result 
print ("final dictionary", str(final_dictionary)) 








