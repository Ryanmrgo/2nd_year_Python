def check_grade(name, roll_number, cse_2040_marks, cse_2050_marks, *var_args, **var_kwargs):
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"CSE-2040 Marks: {cse_2040_marks}")
    print(f"CSE-2050 Marks: {cse_2050_marks}")

    total_marks = cse_2040_marks + cse_2050_marks
    average_marks = total_marks / 2

    print(f"\nTotal Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")

    # Checking grade based on average marks
    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 80:
        grade = 'B'
    elif average_marks >= 70:
        grade = 'C'
    elif average_marks >= 60:
        grade = 'D'
    else:
        grade = 'F'

    print(f"Grade: {grade}")

# Call the function with different student information
check_grade("Sanda", "CSE_061", 85, 90, "Extra Info 1", "Extra Info 2", extra_info="Additional Information")
print("\n----------------------------------\n")
check_grade("Phoo", "CSE_051", 78, 88, "Additional Info 1", "Additional Info 2", extra_info="Extra Information")
