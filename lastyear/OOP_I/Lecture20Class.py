class Student:
    #attribute
    name='Raju'
    age=20
    #actions means functions in here called method
    def printstudentinfo(cls):
        print(cls.name)
        print(cls.age)
S1=Student()
S1.printstudentinfo()
