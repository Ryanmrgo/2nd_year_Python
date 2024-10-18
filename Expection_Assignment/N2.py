
try:
    with open('Expection_Assignment/Cinderell.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Unable to open or read the file.")
else:
    print("File opened successfully.")
