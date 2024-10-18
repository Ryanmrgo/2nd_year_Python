import pickle

class Student:
    def __init__(self, name, roll_number, cse_2040_marks, cse_2050_marks):
        self.name = name
        self.roll_number = roll_number
        self.cse_2040_marks = cse_2040_marks
        self.cse_2050_marks = cse_2050_marks

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

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_number}, " \
               f"CSE-2040 Marks: {self.cse_2040_marks}, CSE-2050 Marks: {self.cse_2050_marks}, " \
               f"Grade Points: CSE-2040: {self.calculate_grade_point(self.cse_2040_marks)}, " \
               f"CSE-2050: {self.calculate_grade_point(self.cse_2050_marks)}"
students = []

# Ask user for input to create student objects
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    roll_number = input(f"Enter roll number of student {i+1}: ")
    cse_2040_marks = int(input(f"Enter CSE-2040 marks of student {i+1}: "))
    cse_2050_marks = int(input(f"Enter CSE-2050 marks of student {i+1}: "))
    student = Student(name, roll_number, cse_2040_marks, cse_2050_marks)
    students.append(student)

with open("student.txt", "wb") as file:
    for student in students:
        pickle.dump(student, file)

# Load students from file and print their detail
with open("student.txt", "rb") as file:
    loaded_students = []
    try:
        while True:
            loaded_student = pickle.load(file)
            loaded_students.append(loaded_student)
    except EOFError:
        pass

for i, student in enumerate(loaded_students, 1):
    print(f"Student {i}: {student}")