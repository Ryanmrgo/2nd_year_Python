import pickle
import Emp

f=open('Emp.dat','wb')
n=int(input('How many Employee'))
for i in range(n):
    id=input('Enter Emp ID')
    name=input('Enter Emp name')
    sal=float(input('Enter Emp sal'))
    e=Emp.Emp(id,name,sal)

    #class object into a byte stream that can be stored into a file
    #Object serialization(pickling) using dump(object,file)
    pickle.dump(e,f)
    
f.close()

print("Unpickling:")
with open('Emp.dat','rb') as f:
    f.seek(0,0)    
    while True:
        try:
            obj=pickle.load(f)
            obj.display()
        except EOFError:
            print('End of file reached')
            break
f.close()


