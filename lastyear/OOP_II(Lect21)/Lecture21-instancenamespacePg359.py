#understanding instance name space


'''
class Student:
    #this is a class var
    n=10

print(Student.n)
Student.n+=1
print(Student.n)



class Student:
    #this is a class var
    n=10
s1=Student()
print('test for class var s1',s1.n)
s2=Student()
print('test for class var s2',s2.n)
'''
class Student:
    #this is a class var
    n=10
s1=Student()
#print('test for class var s1',s1.n)
s1.n+=1
print('test for class var s1',s1.n)
s2=Student()
print(s2.n)

