''''counting the number lines,words, and characters in a file
c1 = cw = cc = 0: Initialize three counters (c1 for lines, cw for words, and cc for characters) to zero.

for line in f:: Iterate through each line in the opened file.

words = line.split(): Split the current line into a list of words using the split() method.

c1 += 1: Increment the line counter by 1 for each line.

cw += len(words): Increment the word counter by the number of words in the current line.

cc += len(line): Increment the character counter by the length of the current line.'''

import os,sys
fname=input('Enter a file name')
if(os.path.isfile(fname)):
   f=open(fname,'r')
else:
    print(fname+'does not exist')
    sys.exit()
c1=cw=cc=0
for line in f:
    words=line.split()
    c1+=1
    cw+=len(words)
    cc+=len(line)
print('no of line:',c1)
print('no of words',cw)
print('no of character:',cc)
f.close
