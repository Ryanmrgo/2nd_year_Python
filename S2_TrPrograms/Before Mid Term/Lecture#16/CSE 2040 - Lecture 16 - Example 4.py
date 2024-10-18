# CSE 2040 - Lecture 16 - Example 4
# Example illustrating loops in Python
'''
print()
# Using while loop in Python
size = int(input('Enter a number: '))
i = 1
factorial = 1
while i <= size:
     factorial = factorial * i
     i = i + 1
print()
print('The factorial of 1 to ',size,'is',factorial)
print('The factorial of 1 to '+str(size)+' is '+str(factorial))

'''
# Using else in while loop - else not reached
code = 'ABCMCA'
slen = len(code)

print()
i = 0
while i < slen:
     if code[i] == 'A' or code[i] == 'B' or code[i] == 'C':
          print('Character found is', code[i])
          print('It is a valid character')
     else:
          print('Parsing of string aborted as unknown character',code[i], 'found')
     i = i + 1
     print()
else:
     print('All parsed characters are valid')
    
