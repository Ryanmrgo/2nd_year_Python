
try:
    x=int(input('Enter a number between 5 and 10'))
    assert x>=5 and x<=10, 'your input is not correct'
    print('The number entered',x)
except AssertionError:
    print('The condition not fullfilled')
'''

try:
    x=int(input('Enter a number between 5 and 10'))
    assert x>=5 and x<=10, 'your input is not correct'
    print('The number entered',x)
except AssertionError as obj:
    print(obj)
'''
