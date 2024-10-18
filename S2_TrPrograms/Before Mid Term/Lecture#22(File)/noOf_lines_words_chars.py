import os, sys
fname=input("Enter File Name: ")

if os.path.isfile(fname):
   print("File exists:", fname)
   f=open(fname, "r")
else:
   print("File does not exist:", fname)
   sys.exit(0)
   
lcount=wcount=ccount=0
for line in f:
   lcount=lcount+1
   ccount=ccount+len(line)
   words=line.split()
   wcount=wcount+len(words)
   
print("The number of Lines:", lcount)
print("The number of Words:", wcount)
print("The number of Characters:", ccount)


'''
str="Hello, how are you"
words=str.split()
print(words)
['Hello,', 'how', 'are', 'you']

#how to find largest words!
#how to search the word "are" is exist or not in the file!
'''
