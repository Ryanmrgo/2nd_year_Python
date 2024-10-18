def even_odd_decorator(func):
    def wrapper(num):
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
        return func(num)
    return wrapper

@even_odd_decorator
def check_number(num):
    print("Number checked.")

# Test the decorator
number = 10
check_number(number)
