#thread communication
from threading import *
from time import *
#create producer class
class Producer:
    def __init__(self):
        self.lst=[]
        self.cv=Condition()
    def produce(self):
        #lock the contion object
        self.cv.acquire()
        #create 1 to 10 items
        for i in range(1,11):
            self.lst.append(i)
            sleep(0.1)
            print('Item produced')
        #inform the consumer that production is completed
        self.cv.notify()
        #release the lock
        self.cv.release()
        
class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        #get lock on condition object
        self.prod.cv.acquire()
        #wait only for 0 seconds after produce
       # self.prod.cv.wait(timeout=0)
        #releae the lock
        self.prod.cv.release()
        #display the content of list
        print('Item Consumed',self.prod.lst)
'''
        #sleep till dataprodover is false
        while self.prod.dataprodover==False:
            sleep(0.1)
            #display the conternt of list when dataproduct is over
            #print(self.prod.lst)
        print(self.prod.lst)
'''
#create producer object
p=Producer()
#create consumer object
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()




            
