'''Reading an existing text file
      read() → To read total data from the file.
      read(n) → To read ‘n’ characters from the file.
      readline() → To read only one line.
      readlines() → To read all lines into a list.

'''

fp = open("demofile.txt", "r")
'''
#fp = open("D:\\myfiles\welcome.txt", "r")
print(fp.read())
print(fp.read(5))

#You can return one line by using the readline() method
print(fp.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
for x in fp:
  print(x)

'''
#reading multiple lines
lines=fp.readlines()
#print(lines)

for line in lines:
   print(line, end='')

#Note: You should always close your files, in some cases, due to buffering,
#changes made to a file may not show until you close the file.
fp.close()
