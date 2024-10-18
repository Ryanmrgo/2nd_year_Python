def apply_function_to_list(func):
    def decorator(lst):
        result = []
        for x in lst:
            result.append(func(x))
        print(','.join(map(str, result)))
    return decorator


@apply_function_to_list
def square(x):
    return x * x


my_list = [1, 2, 3, 4, 5]

square(my_list)
