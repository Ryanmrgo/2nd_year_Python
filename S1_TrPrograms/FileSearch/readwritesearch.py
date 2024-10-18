# Writing to a file
with open('example_file.txt', 'w') as file:
    file.write("This is an example file.\n")
    file.write("It contains some text for demonstration purposes.\n")
    file.write("Let's see how we can read and search for a specific word.\n")

    file.write("Today lecture is for file handling.\n")

# Reading from the file and searching for a word
search_word = 'ss'

with open('example_file.txt', 'r') as file:
    content = file.read()
    
    if search_word in content:
        print(f"The word '{search_word}' is present in the file.")
    else:
        print(f"The word '{search_word}' is not found in the file.")

