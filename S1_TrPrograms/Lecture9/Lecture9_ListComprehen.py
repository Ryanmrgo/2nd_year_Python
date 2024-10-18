#Lecture10
#List Comprehension
#num=[1,2,3,4]
#print('10 times for num',10*num)

#illustration of list comprehension
even=[i for i in range(50) if i%2==0]
print(even)
odd=[i for i in range(50) if i%2!=0]
print(odd)


test1=[x for x in range(1,11)]
print('Test1 result',test1)
test2=[x for x in range (1,11) if x%2==0]
print('Test2 result',test2)
test3=[x if x>2 else x+1 for x in range(1,11)]
print('Test3 result',test3)

'''
#comprehen
num_comprehension=[x*10 for x in num]
print(num_comprehension)
'''

#check for words
words=['hello','a','cynthia']
words_comprehension=[x.upper()for x in words]
print(words_comprehension)


str1="cynthia34568"
digit_comprehension=[x for x in str1 if x.isdigit()]
alpha_comprehension=[x for x in str1 if x.isalpha()]
print(digit_comprehension)
print(alpha_comprehension)

#list1=[[1,2,3],[4,5,6],['a','b']
#mytest[0]=[x[0] for x in list1]
#print(mytest[0])


 

