#Creating Dictionary using tuple
dictionary2 = dict(A=65,B=66,C=67,D=68)
for key,value in dictionary2.items():
     print('ASCII Code of',key,'is',value)
#Creating dictionary using tuple
# Creating dictionaries using a tuple
print()
dictionary1={'Student X':('A','B','B'), 'Student Y':('A','A','A-')}
print('for dict1',dictionary1)

print()
dictionary2={('Student X','Student Y', 'Student Z'):'A',('Student A','Student B', 'Student C'):'B'}
print('for dict2',dictionary2)

print()
for key,value in dictionary1.items():
     print('using looping',key,value)
#printing data using nested loop and len() for print dictionary
players={('M1','M2','M3'):(22,23,22),('I1','I2','I3'):(21,19,23)}
print(players)
print()
for key,value in players.items():
     print()
     for i in range(len(key)):
          print('The age of player', key[i],'is',value[i])
