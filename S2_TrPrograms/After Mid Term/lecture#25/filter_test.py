'''
def is_even(x):
    if x%2==0:
        return True
    else:
        return False

lst=[10,23,45,46,70,99]
lst1=list(filter(is_even,lst))
print(lst1)

'''

lst = [10,23,45,46,70,99]
lst1 = list(filter(lambda x: (x%2 == 0), lst))
print(lst1)
