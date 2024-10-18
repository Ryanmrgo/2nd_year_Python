#Lecture10#tuple Mehtods# vowels tuple
'''
vowels = ('a', 'e', 'i', 'o', 'i', 'o', 'e', 'i', 'u')
# count element 'i'
count = vowels.count('i')
print (count)
print('The count of i is:', count)
count = vowels.count('I')
print('The count of I is:', count)
count = vowels.count('p')
print('The count of p is:', count)
''''

#Illustration of in operator with tuple
for str in ('Bread','Butter','Jam'):
    print('I love',str)
  
tuple len   
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print ("First tuple length : ", len(tuple1))
print ("Second tuple length : ", len(tuple2))


#tuple sum()
numbers = [2.5, 3, 4, -5]
# start parameter is not provided
numbersSum = sum(numbers)
print(numbersSum)
#start = 10
numbersSum = sum(numbers, 10)
print(numbersSum)


#tuple
my_tuple = 3, 4.6, "dog"
print(my_tuple)  
# tuple unpacking is also possible
a, b, c = my_tuple
print(a)      # 3
print(b)      # 4.6 
print(c)      # dog





