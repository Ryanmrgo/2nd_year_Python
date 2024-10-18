'''Pickling & Unpickling'''

from pickle import *

class person:
   def __init__(self):
      self.name="XYZ"
      self.age=22
   def show(self):
      print ("name:", self.name, "age:", self.age)

      
p1=person()

f=open("data.txt","wb")
dump(p1,f)
f.close()
print ("unpickled")
f=open("data.txt","rb")
p1=load(f)
p1.show()
