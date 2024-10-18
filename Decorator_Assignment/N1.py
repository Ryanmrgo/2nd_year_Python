def printer_decorator(what_to_print):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{what_to_print}: {result}")
            return result
        return wrapper
    return decorator

@printer_decorator("Course")
def print_course(course_name, course_credits):
    return { "Course Name": course_name, "Course Credits": course_credits }

@printer_decorator("Country and Capital")
def print_country(country, capital):
    return { "Country": country, "Capital": capital }

@printer_decorator("Word and Synonyms")
def print_synonyms(word, synonyms):
    return { "Word": word, "Synonyms": synonyms }

@printer_decorator("Grade and Grade Points")
def print_grade(grade, grade_points):
    return { "Grade": grade, "Grade Points": grade_points }

# Test Cases
print_course("ProgrammingII", 5)
print_course("Electronic", 4)
print_course("Physics", 4)
print_course("Mathematics", 5)

print_country("England", "London")
print_country("Greece", "Athens")
print_country("Myanmar", "Yangon")
print_country("India", "Delhi")



print_synonyms("Nice", ["Welcome", "Cordial"])
print_synonyms("Cool", ["Chill", "Wintry","Coldish"])
print_synonyms("Rest", ["Vacation", "Break","Siesta"])

print_grade("A", 5.0)
print_grade("B", 4.0)
print_grade("C", 3.0)
print_grade("D", 2.0)
print_grade("E", 1.0)

