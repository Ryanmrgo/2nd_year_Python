class Student:
    	# Class variable
    school_name = 'Myanamr Institute of Information Technology'
	#instance variable
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def __str__(self):
          return str(self.name)+'\n'+str(self.roll_no)+'\n'+str(Student.school_name)

# create first object
s1 = Student('Aye Aye', 10)
print(s1)

#print(s1.name, s1.roll_no, Student.school_name)
#access class variable

#create second object
s2 = Student('Latt Latt', 20)
#access class variable
print(s2)
#print(s2.name, s2.roll_no, Student.school_name)


