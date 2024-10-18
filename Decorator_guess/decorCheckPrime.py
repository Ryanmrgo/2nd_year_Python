def prime_checker_decorator(func):
    def wrapper(num):
        if num < 2:
            print(f"{num} is not a prime number.")
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                return False
        print(f"{num} is a prime number.")
        return func(num)
    return wrapper

@prime_checker_decorator
def check_prime(num):
    print("Prime number checked.")

# Test the decorator
number = 17
check_prime(number)
