# Check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the string with its reverse
    return s == s[::-1]

# Test the function
string = "A man, a plan, a canal, Panama!"
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
