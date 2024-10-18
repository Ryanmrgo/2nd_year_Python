'''
These strings are called f-strings. The f is for format, because Python
formats the string by replacing the name of any variable in braces with
its value. The output from the previous code is:
'''
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

'''
F-strings were first introduced in Python 3.6. If you’re using Python 3.5 or
earlier, you’ll need to use the format() method rather than this f syntax. To
use format(), list the variables you want to use in the string inside the
parentheses following format. Each variable is referred to by a set of braces;
the braces will be filled by the values listed in parentheses in the order
provided:
full_name = "{} {}".format(first_name, last_name)
'''
first_name = "ada"
last_name = "lovelace"
full_name = "{} {}".format(first_name, last_name)
print(full_name)
message = "One of Python's strengths is its diverse community."
print(message)
#message = 'One of Python's strengths is its diverse community.'
#print(message)
