# Example illustrating reading from and writing to files in Python

# Reading from a file

print()
print('Reading from a file called myfile.txt ...')
file1 = open("mytestfile1.txt","r")
print('------------------------------------------------------------')
line1 = file1.read()
print(line1)
print("current position1 using ",file1.seek(234))
print("current position1 using tell",file1.tell())
file1.close()

'''
print('------------------------------------------------------------')
print('The file pointer is at ', end = '')
print("current position1",file1.tell())



print()
print('Moving the file pointer to ', end = '')
print(file1.seek(25))
#file1.close()
#file1.close()

print("current position1",file1.tell())
print('------------------------------------------------------------')
file1.close()

print('seek test0',file1.seek(0))

print("current position1",file1.tell())
print('------------------------------------------------------------')

line2 = file1.read()
print(line2)
print('------------------------------------------------------------')

print()
print('Moving the file pointer to ', end = '')
print(file1.seek(0))
print('------------------------------------------------------------')
line3 = file1.read()
print(line3)
print('------------------------------------------------------------')


# Write to a file
file2 = open("newprogram1.txt","w")
file2.write("This is a new file")
file2.write("I am testing my test file")
file2.write("mytestfile.txt")



#print('New file named newfile.txt created. Check your current folder for the file')
#print()

# Closing files
#file1.close()
#file2.close()

'''



