f=open('mytestfile1.txt','a+')
print('Enter @ at end of the text')
while(str!='@'):
    str=(input('Enter text'))
    if(str!='@'):
        f.write(str+ '\n')
f.seek(0,0)
mystr=f.read()
print(mystr)
f.close()
f.close()
