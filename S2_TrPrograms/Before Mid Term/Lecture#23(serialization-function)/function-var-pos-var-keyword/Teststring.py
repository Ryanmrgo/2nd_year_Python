#a function to find total and average
def display(lst):
    '''To find total and average'''
    for value in lst:
        print('loop var',value)

#take a group of integers from keyboard
print('Enter number separated by comma')
lst=[x for x in input().split(',')]
print(lst)
ee=display(lst)
print(ee)

