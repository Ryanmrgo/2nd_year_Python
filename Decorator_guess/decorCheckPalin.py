def palindrome_checker_decorator(func):
    def wrapper(string):
        if string == string[::-1]:
            print(f"'{string}' is a palindrome.")
        else:
            print(f"'{string}' is not a palindrome.")
        return func(string)
    return wrapper

@palindrome_checker_decorator
def check_palindrome(string):
    print("Palindrome checked.")

# Test the decorator
test_string = "radar"
check_palindrome(test_string)
