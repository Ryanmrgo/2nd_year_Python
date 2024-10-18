'''
#Lecture 13, File read no Encoding
f=open("guidobio.txt",'r')
print(f.read(),end='')
f.close()

try:
    f=open("guidobio.txt",'r')
    print(f.read(),end='')
except:
        f.close()

'''
try:
    f=open("guidobio.txt",'r')
    print(f.read(),end='')
finally:
        f.close()

