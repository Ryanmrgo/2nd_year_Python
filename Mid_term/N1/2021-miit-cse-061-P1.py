import pickle

class Student:
    def __init__(self, name, roll_number, cse_2040_marks, cse_2050_marks,cse_2060_marks):
        self.name = name
        self.roll_number = roll_number
        self.cse_2040_marks = cse_2040_marks
        self.cse_2050_marks = cse_2050_marks
        self.cse_2060_marks = cse_2060_marks

    def calculate_grade_point(self, marks):
        if marks >= 90:
            return 4.0
        elif 80 <= marks < 90:
            return 3.5
        elif 70 <= marks < 80:
            return 3.0
        elif 60 <= marks < 70:
            return 2.5
        elif 50 <= marks < 60:
            return 2.0
        elif 40 <= marks < 50:
            return 1.5
        else:
            return 0.0
        

    def calculate_average_mark(self,cse_2040_marks, cse_2050_marks,cse_2060_marks):
        avg=(self.cse_2060_marks+cse_2040_marks+cse_2050_marks)/3
        
        return avg



    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_number}, " \
               f"CSE-2040 Marks: {self.cse_2040_marks}, CSE-2050 Marks: {self.cse_2050_marks},CSE-2060 Marks: {self.cse_2060_marks},  " \
               f"Grade Points: CSE-2040: {self.calculate_grade_point(self.cse_2040_marks)}, " \
               f"Grade Points: CSE-2050: {self.calculate_grade_point(self.cse_2050_marks)}, " \
               f"Grade Points: CSE-2060: {self.calculate_grade_point(self.cse_2060_marks)}," \
               f"Average marks of student: {self.calculate_average_mark(self.cse_2040_marks,self.cse_2050_marks,self.cse_2060_marks)}"
students = []


num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input(f"Enter student name {i+1}: ")
    roll_number = input(f"Enter roll number{i+1}: ")
    cse_2040_marks = int(input(f"Enter marks for subject 1 of student {i+1}: "))
    cse_2050_marks = int(input(f"Enter marks for subject 2 of student {i+1}: "))
    cse_2060_marks = int(input(f"Enter marks for subject 3 of student {i+1}: "))
    student = Student(name, roll_number, cse_2040_marks, cse_2050_marks,cse_2060_marks)
    students.append(student)

with open("student.txt", "w") as file:
    for student in students:
        file.write(str(student))

# # Load students from file and print their detail
# with open("student.txt", "r") as file:
#     loaded_students = []
#     try:
#         while True:
#             loaded_student = file.read
#             loaded_students.append(loaded_student)
#     except EOFError:
#         pass

# for i, student in enumerate(loaded_students, 1):
#     print(f"Student {i}: {student}")



with open("studentb.txt", "wb") as file1:
    for student in students:
        pickle.dump(student, file1)

# Load students from file and print their detail
with open("studentb.txt", "rb") as file1:
    loaded_students = []
    try:
        while True:
            loaded_student = pickle.load(file1)
            loaded_students.append(loaded_student)
    except EOFError:
        pass

for i, student in enumerate(loaded_students, 1):
    print(f"Student {i}: {student}")


sroll_number= int(input("Enter roll number to check: "))
content=file.read()
if sroll_number in content:
    print(sroll_number+"is present.")
else:
    print(sroll_number+"is not present.Error!")

