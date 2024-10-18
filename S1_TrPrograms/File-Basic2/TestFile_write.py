'''
#Writing Data to the file
f=open('mytestfile.txt','w')
mystr=input('Enter the text')
f.write(mystr)
f.close()


#Reading data to the file
f=open('mytestfile.txt','r')
mystr=f.read()
print(mystr)
f.close()


f=open('mytestfile1.txt','w')
print('Enter @ at end of the text')
while(str!='@'):
    str=(input('Enter text'))
    if(str!='@'):
        f.write(str+ '\n')
f.close()

f=open('mytestfile1.txt','a+')
print('Enter @ at end of the text')
while(str!='@'):
    str=(input('Enter text'))
    if(str!='@'):
        f.write(str+ '\n')
#f.seek(0,0)
f.close()
'''
f=open('mytestfile1.txt','r')
mystr=f.read()
print(mystr)
f.close()



