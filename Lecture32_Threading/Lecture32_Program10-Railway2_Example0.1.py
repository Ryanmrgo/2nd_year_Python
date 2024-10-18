#multitasking using two threads
from threading import *
from time import *
class Railway:
    #constructor that accepts no.of available berths
    def __init__(self,available):
        self.available=available
        #create a lock object
        self.l=Lock()
    #a method that reserves berth
    def reserve(self,wanted):
        #lock the current object
        self.l.acquire()
        #display no.of avaialable berths
        print('Available no.of berths \n',self.available)
        #if available>=wanted, allot them
        if(self.available>=wanted):
            #find thread name
            name=current_thread().getName()
            #display berth is alloted for the person
            print('%d berths alloted for %s \n'%(wanted,name))
            #make time delay
            sleep(0.5)
            #decrease the no.of available birth
            self.available-=wanted
        else:
            #if available<wanted
            print('Sorry, no berth allot \n')
            #task is completed, release the lock
        self.l.release()
#create instance to railway class
#specity only one berth is available
obj=Railway(3)
#create two threads and specify 1 berth is needed
t1=Thread(target=obj.reserve, args=(1,))
t2=Thread(target=obj.reserve, args=(2,))
#give names to the threads
t1.setName('First Preson')
t2.setName('Second Preson')
#run the threads
t1.start()
t2.start()



