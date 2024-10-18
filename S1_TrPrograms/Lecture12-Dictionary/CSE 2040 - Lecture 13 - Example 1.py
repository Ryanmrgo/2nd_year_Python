# CSE 2040 - Lecture 13 - Example 1
# Example illustrating more examples using dictionaries



# Creating dictionaries using a tuple
     
# Value is a tuple
student_grade ={'Student X':('A','B','B'), 'Student Y':('A','A','A-')}
grade_student = {'A':('Student X','Student Y', 'Student Z')}

print()
print("Grades (value) of a student stored as a tuple:")
for key,value in student_grade.items():
     print(key,value)

print()
print("Students (value) for a grade stored as a tuple:")
for key,value in grade_student.items():
     print(key,value)

# Key as a tuple
registered_students = {("S1","S2","S5"):"CSE-2040",("S61","S62","S63"):"ECE-2040"}
print()
print("Registered students (key) of a course stored as a tuple:")
for key,value in registered_students.items():
     print(key,value)

# Value as a sub list
function_variables = {"f1": {"var1": 10, "var2": "X"},"f2": {"var1": 100, "var2": "Y"}}
print()
print("Variables (value) of functions stored as a sub list:")
for key,value in function_variables.items():
     print(key,value)

print()

