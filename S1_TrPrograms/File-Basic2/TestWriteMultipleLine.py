f=open('mytestfile1.txt','w')
print('Enter @ at end of the text')
while(str!='@'):
    str=(input('Enter text'))
    if(str!='@'):
        f.write(str+ '\n')

