'''
f1=open('cat.jpg','rb')
print(f1)
#f1.close()

f2=open('new.jpg','wb')
bytes1=f1.read()
f2.write(bytes1)
print(f2)
f1.close()
f2.close()
'''
f1=open('cat.jpg','rb')
f2=open('newcat.jpg','wb')
readbytes=f1.read()
f2.write(readbytes)
print(f2)
f1.close()
f2.close()

