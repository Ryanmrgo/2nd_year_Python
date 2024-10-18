
import pickle
import Emp
'''
f=open('Emp.dat','wb')
n=int(input('How many Employee'))
for i in range(n):
    id=input('Enter Emp ID')
    name=input('Enter Emp name')
    sal=float(input('Enter Emp sal'))
    e=Emp.Emp(id,name,sal)
    pickle.dump(e,f)
f.close()
'''
#f=open('C://Users//MIIT-ITSM02//Desktop//Pickle&Unpickle//Emp.dat','rb')

f=open('C://Users//MIIT-ITSM02//Desktop//Lecture12//Emp.dat','rb')

with open('Emp.dat','rb') as f:
    f.seek(0,0)    
    while True:
        try:
        #f.seek(0)
            
            obj=pickle.load(f)
            obj.display()
        except EOFError:
            print('End of file reached')
            break
f.close()


