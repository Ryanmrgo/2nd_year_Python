# Lecture 14 - Example 2
# Working with var-postional and var-keyword parameters

def display(batch, *courses, academic_year = 2020, **grades):
    print(batch)
    print(academic_year)
    print()
    print("Printing contents of the var-positional parameter courses")
    for course in courses:
        print(course)
    print()
    for student,grades in grades.items():
        print(student + " - " + str(grades))
# Main
display("2018","Programming I", "Programming II", "Programming III", academic_year = 2020,RXX1 = ["A","B+","A"], RXX9 = ["A-","B","C+"])
