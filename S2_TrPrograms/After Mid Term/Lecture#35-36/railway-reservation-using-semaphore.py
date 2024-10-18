#railway reservation
#multitasking using two threads

from threading import *
from time import *

class Railway:
    def __init__(self,available):
        self.available = available
        #self.l = Lock()   #create a lock object
        self.l = Semaphore()
    def reserve(self,wanted):
        self.l.acquire()  #lock the current object
        print('Available no of breths= ',self.available)
        if (self.available>=wanted):
            name = current_thread().getName()
            print('%d breths allotted for %s' %(wanted,name))
            sleep(1.5)
            self.available-=wanted
        else:
            print('Sorry no breths to allot')
            
        self.l.release() #task is completed, release the lock
                
obj=Railway(1)
t1=Thread(target=obj.reserve,args=(1,))
t2=Thread(target=obj.reserve,args=(1,))
t1.setName("First Person")
t2.setName("Second Person")
t1.start()
t2.start()

