from sys import intern
mytest1 = 'Wednesday is funday'
mytest2= 'Wednesday is funday'
print('comparison operator test',id(mytest1==mytest2))
print('indentity  operator test',id(mytest1 is mytest2))
print(' intern and comparison operator test',intern(mytest1)==intern(mytest2))
print(' intern and indentity operator test',intern(mytest1) is intern(mytest2))
print(' intern and comparison operator id test',id(intern(mytest1)==intern(mytest2)))
print(' intern and indentity operator id test',id(intern(mytest1) is intern(mytest2)))






