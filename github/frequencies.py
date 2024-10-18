
def  frequencies(input_string):


    frequency_dict = {}
    
    for char in input_string:

        if char in frequency_dict:

            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    

    return frequency_dict

# Input

input_string = input("Enter a string: ")

# Character frequency dictionary

frequency_dict = frequencies(input_string)

# Printing the output dictionary
print(frequency_dict)
