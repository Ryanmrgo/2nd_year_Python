class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def show(self):
        print('Inside instance method')
        print("Name:",self.name,", Roll_no:",self.roll_no,", School name:",self.school_name)
        print(Student.school_name)

# create Object
s1 = Student('Emma',10)
s1.show()
print('Outside class')
# access class variable outside class
# access using object reference
print(s1.school_name)
# access using class name
print(Student.school_name)
