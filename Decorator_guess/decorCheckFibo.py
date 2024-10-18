def fibonacci_checker_decorator(func):
    def wrapper(num):
        if num <= 0:
            print("Cannot calculate Fibonacci sequence for non-positive numbers.")
            return None
        else:
            return func(num)
    return wrapper

@fibonacci_checker_decorator
def calculate_fibonacci(num):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < num:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    print(f"The Fibonacci sequence up to {num} terms is: {fibonacci_sequence}")
    return fibonacci_sequence

# Test the decorator
number_of_terms = 10
calculate_fibonacci(number_of_terms)
