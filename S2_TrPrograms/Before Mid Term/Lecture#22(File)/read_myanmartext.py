'''reading myanmar text, UTF stands for “Unicode Transformation Format”,
and the '8' means that 8-bit values are used in the encoding'''

with open('myanmartext.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    for line in content:
        print(line,end='')
