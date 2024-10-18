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

student1 = Student("Sanda", "CSE_061", 85, 90)
student2 = Student("Phoo", "CSE_051", 78, 88)
student3 = Student("Charlie", "CSE_012", 92, 95)

with open("student.txt", "wb") as file:
    pickle.dump(student1, file)
    pickle.dump(student2, file)
    pickle.dump(student3, file)

with open("student.txt", "rb") as file:
    loaded_student1 = pickle.load(file)
    loaded_student2 = pickle.load(file)
    loaded_student3 = pickle.load(file)

print("Student 1:", loaded_student1)
print("Student 2:", loaded_student2)
print("Student 3:", loaded_student3)
