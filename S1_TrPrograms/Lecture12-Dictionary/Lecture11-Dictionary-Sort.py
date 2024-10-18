
#sort a dict by key
mydict = {
    "carl": 40,
    "alan": 2,
    "bob": 1,
    "danny": 3,
}
#sort a dict by key
#before sorted
#for key in mydict.keys():
#    print( (key, mydict[key]))

#after sorted
for key in sorted(mydict.keys()):
    print( (key, mydict[key]))

'''
#sort a dict by value
for key, value in sorted(mydict.items(), key=lambda item: item[1]):
    print((key, value))
'''
'''
#A lambda function that adds 10 to the number passed in as an
#argument, and print the result:
x = lambda a : a + 10
print(x(5))
#updating dict
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
Dict.update({"Sarah":9})
print(Dict)
#items return key value pair in python
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}	
print("Students Name: %s" % list(Dict.items()))
'''
'''
#not yet tested the result
#keys in Dict ,Check if a given key already exists in a dictionary
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boys = {'Tim': 18,'Charlie':12,'Robert':25}
Girls = {'Tiffany':22}
for key in list(Dict.keys()):
    if key in list(Boys.keys()):
        print(True)
    else:       
        print(False)

'''





