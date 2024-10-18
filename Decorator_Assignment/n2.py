def sum_it_up(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        total = sum(args)
        print(f"Sum of the series {args}: {total}")
        return result
    return wrapper

@sum_it_up
def series_sum(*args):
    return sum(args)


series_sum(1, 2, 3, 4, 5)
series_sum(2, 4, 6, 8, 10)
series_sum(1, 3, 5, 7, 9, 11)
