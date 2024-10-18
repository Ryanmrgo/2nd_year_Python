class Student:
    n=10

s1=Student()
print("n of s1:",s1.n)

#n+=10
s1.n+=10
print("n of s1 after modify:",s1.n)

s2=Student()
print("n of s2:",s2.n)

s2.n+=30
print("n of s2 after modify:",s2.n)

print(Student.n)
