#python program using two threads
from threading import *
from time import *
class Theatre:
    #constructor that accept a string
    def __init__(self,str):
        self.str=str
    #a method that repeats for 5 tickets
    def movieshow(self):
        for i in range (1,6):
            print('two threads run simultaneously \n')
            print(self.str,':',i,'\t')
            #sleep(0.1)
#create two instances to Theatre class
obj1=Theatre('cut tickets \n')
obj2=Theatre('show chair \n')
#create two threds to run movieshow
print('creating two threads')
t1=Thread(target=obj1.movieshow)
t2=Thread(target=obj2.movieshow)
print('T1 is started')
t1.start()
print('T2 is started')
t2.start()
