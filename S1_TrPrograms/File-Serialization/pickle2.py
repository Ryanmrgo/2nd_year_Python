import pickle

# Read the serialized data from the file
with open('serialized_data.pkl', 'rb') as file:
    serialized_data = file.read()

# Deserialize the byte stream back to the original object
deserialized_data = pickle.loads(serialized_data)

# Display the deserialized data
print(deserialized_data)
