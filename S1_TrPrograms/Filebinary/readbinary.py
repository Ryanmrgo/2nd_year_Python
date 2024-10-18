#Lecture 13
#reading a binary

import os
'''
with open('cat.jpg','rb') as rf:
       with open('new1','wb') as wf:
          for line in rf:
                 wf.write(line)
f=open('new1','rb')
for i in f:
       print(i)
f.close()
'''

#using open
f=open('cat.jpg','rb')
for i in f:
       print(i)
f.close()



