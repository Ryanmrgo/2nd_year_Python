import pickle

# Example object to serialize
data_to_serialize = {'name': 'John', 'age': 30, 'city': 'New York'}

# Serialize the object to a byte stream
serialized_data = pickle.dumps(data_to_serialize)

# Save the serialized data to a file
with open('serialized_data.pkl', 'wb') as file:
    file.write(serialized_data)
