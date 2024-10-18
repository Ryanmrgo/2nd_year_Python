def factorial_checker_decorator(func):
    def wrapper(num):
        if num < 0:
            print("Cannot calculate factorial for negative numbers.")
            return None
        elif num == 0:
            print("Factorial of 0 is 1.")
            return 1
        else:
            return func(num)
    return wrapper

@factorial_checker_decorator
def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")
    return factorial

# Test the decorator
number = 5
calculate_factorial(number)
