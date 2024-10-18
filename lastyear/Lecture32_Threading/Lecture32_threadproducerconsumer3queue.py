#thread communication using queue
from threading import *
from time import *
from queue import *
#create producer class
class Producer:
    def __init__(self):
        self.q=Queue()
    def produce(self):
            #create 1 to 10 items
        for i in range(1,11):
            print('item produced:',i)
            self.q.put(i)
            sleep(0.1)
        
class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        #receive 1 to 10 items
        for i in range(1,11):
            print('items consumed',self.prod.q.get(i))
#create producer object
p=Producer()
#create consumer object
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()


'''



        #get lock on condition object
        self.prod.cv.acquire()
        #wait only for 0 seconds after produce
       # self.prod.cv.wait(timeout=0)
        #releae the lock
        self.prod.cv.release()
        #display the content of list
        print(self.prod.lst)
        
        #sleep till dataprodover is false
        while self.prod.dataprodover==False:
            sleep(0.1)
            #display the conternt of list when dataproduct is over
            #print(self.prod.lst)
        print(self.prod.lst)
'''
            
