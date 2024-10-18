#var positional arguments
def sum(*args):
    total = 0
    for num in args:
        total = total + num
    return total
print(sum(1,2,3,45,3,234,56,78,34,56,89,90))
