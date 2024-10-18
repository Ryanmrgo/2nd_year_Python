#Multi Tasking using two threads
from threading import *
from time import *
class Railway:
    #constructor that accepts no.of available berths
    def __init__(self,available):
        self.available=available
    #a method that reserves berth
    def reserve(self,wanted):
        #display no of available berth
        print('Available no.of berths= \t',self.available)
        #if available>=wanted,allot them
        if(self.available>=wanted):
            #find the thread name
            name=current_thread().getName()
            #display birth is alloted for the person
            print('%d berths alloted for %s \t',wanted,name)
            #make time delay
            sleep(1.5)
            #decrease no.of avaliable berths
            self.available-=wanted
        else:
            print('Sorry no berth are alloted ')
#create instance of railway
#specify only one birth is ava
obj=Railway(1)
#create two threads and specity 1 berth is need
t1=Thread(target=obj.reserve,args=(1,))
t2=Thread(target=obj.reserve,args=(1,))
#give names to threads
t1.setName('First Person: \t')
t2.setName('Second Person: \t')
#run the threads
t1.start()
t2.start()
#t1.join()
#t2.join()




 
