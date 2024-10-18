marklist = {
   "Mahesh" : {"Phy" : 60, "maths" : 70},
   "Madhavi" : {"phy" : 75, "maths" : 68},
   "Mitchell" : {"phy" : 67, "maths" : 71}
}
for k,v in marklist.items():
   print (k, ":", v)

#to access value from an inner dictionary with [] notation or get() method
obj=marklist['Mahesh']
#print(obj)
print (obj.get('Phy'))
print (obj.get('maths'))



#dic={1:"A",2:"B"}
#print (dic[1])


#print (marklist['Mitchell'].get('phy'))
#print (marklist['Mitchell'].get('maths'))

'''
A dictionary in Python is an object of the built-in dict class, which defines the following methods −
Sr.No. 	Method and Description

dict.clear()

Removes all elements of dictionary dict.
 	
dict.copy()

Returns a shallow copy of dictionary dict.
 	
dict.fromkeys()

Create a new dictionary with keys from seq and values set to value.
 	

dict.get(key, default=None)

For key key, returns value or default if key not in dictionary.
	

dict.has_key(key)

Returns true if a given key is available in the dictionary, otherwise it returns a false.
	

dict.items()

Returns a list of dict's (key, value) tuple pairs.
	

dict.keys()

Returns list of dictionary dict's keys.
	

dict.pop()

Removes the element with specified key from the collection
	

dict.popitem()

Removes the last inserted key-value pair
 	

dict.setdefault(key, default=None)

Similar to get(), but will set dict[key]=default if key is not already in dict.
 	

dict.update(dict2)

Adds dictionary dict2's key-values pairs to dict.
	

dict.values()

Returns list of dictionary dict's values.
'''
