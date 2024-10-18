import pickle

class Student:
    def __init__(s, name, roll_number, cse_2040_marks, cse_2050_marks):
        s.name = name
        s.roll_number = roll_number
        s.cse_2040_marks = cse_2040_marks
        s.cse_2050_marks = cse_2050_marks

    def __str__(s):
        return f"Name: {s.name}, Roll No: {s.roll_number}, CSE-2040 Marks: {s.cse_2040_marks}, CSE-2050 Marks: {s.cse_2050_marks}"

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
