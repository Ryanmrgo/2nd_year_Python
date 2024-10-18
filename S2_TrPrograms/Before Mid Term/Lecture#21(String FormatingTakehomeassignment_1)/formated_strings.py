#String Format
#combine strings and numbers like this
age = 36
txt = "My name is John, I am " + str(age)
print(txt)


#To display string like that using format()-> We are the knights who say "Ni!"
#print('We are the {} who say "{}!"'.format('knights', 'Ni'))
#To display string like that using format()-> spam and eggs
#print('{0} and {1}'.format('spam', 'eggs'))
#print('{1} and {0}'.format('spam', 'eggs'))


#combine strings and numbers by using the format() method
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) 

'''    
Formatted string literals:

year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

'''
