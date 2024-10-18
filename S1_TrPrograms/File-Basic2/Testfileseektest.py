print('Reading from a file called myfile.txt ...')
file1 = open("myfile.txt","r")
print('------------------------------------------------------------')
line1 = file1.read()
print(line1)
#file1.close()


print('------------------------------------------------------------')
print('The file pointer is at ', end = '')
print("current position1",file1.tell())



print()
print('Moving the file pointer to ', end = '')
print(file1.seek(2))
file1.close()
