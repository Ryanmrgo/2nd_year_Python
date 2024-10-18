'''
string methods to change case:
    lower(): Converts a string to lowercase.
    upper(): Converts a string to uppercase.
    title(): Converts the first character of each word to uppercase.
'''
'''
#Solutions 
# 2-3. Personal Message
person_name = "Eric"
personal_message = f"Hello {person_name}, would you like to learn some Python today?"
print(personal_message)

# 2-4. Name Cases
name = "John Doe"

# Lowercase
lowercase_name = name.lower()
print(f"Lowercase: {lowercase_name}")

# Uppercase
uppercase_name = name.upper()
print(f"Uppercase: {uppercase_name}")

# Title case
titlecase_name = name.title()
print(f"Title Case: {titlecase_name}")

#2-5 Print the quote and the name of its author
print('Albert Einstein once said')
print('"A person who never made a mistake never tried anything new."')

#2-6 Print the quote and the name of its author using variables: famous_person, message
famous_person='Albert Einstein once said'
message='A person who never made a mistake never tried anything new.'
print(f'Famous Person Name: {famous_person}')
print(f'Quote: "{message}"')

'''
#2-7 Stripping Names
name = "\tEric Matthes\n"
print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())


