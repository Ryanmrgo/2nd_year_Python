def is_palindrome(input):

    cleaned_string = ''.join(char.lower() for char in input if char.isalnum())

    
    return cleaned_string == cleaned_string[::-1]


# input from the user
input = input("Enter a string: ")

# Check palindrome
if is_palindrome(input):
    print("The Input string is a Palindrome.")
else:
    print("The Input string is not a Palindrome.")