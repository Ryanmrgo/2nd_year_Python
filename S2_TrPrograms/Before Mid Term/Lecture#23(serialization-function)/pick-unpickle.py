import pickle
'''
#pickling and unpickling using file
data = {"name": "John", "age": 25}
with open("data.pkl", "wb") as file:    
	pickle.dump(data, file)


with open("data.pkl", "rb") as file:    
	loaded_data = pickle.load(file)
	print(loaded_data)


'''
#pickling and unpickling not using file
data = {"name": "Jane", "age": 30} 
serialized_data = pickle.dumps(data)

loaded_data = pickle.loads(serialized_data)
print(loaded_data)

