'''Following program pickle a dictionary object into a binary file.'''

import pickle
f=open("data.txt","wb")
dct={"name":"Ravi", "age":23, "Gender":"M","marks":75}
pickle.dump(dct,f)
f.close()

'''
When the code is executed,
the dictionary object's byte representation will be stored in data.txt file.

To unpickle or deserialize data from a binary file back to dictionary,
run following program.

'''
f=open("data.txt","rb")
d=pickle.load(f)
print (d)
f.close()
