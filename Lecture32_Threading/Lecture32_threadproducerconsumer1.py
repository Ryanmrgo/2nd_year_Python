#thread communication
from threading import *
from time import *
#create producer class
class Producer:
    def __init__(self):
        self.lst=[]
        self.dataprodover=False
    def produce(self):
        #create 1 to 10 items
        for i in range(1,11):
            self.lst.append(i)
            sleep(0.5)
            print('Item produced \n')
        #inform the consumer that datat production is completed
        self.dataprodover=True
class Consumer:
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        #sleep till dataprodover is false
        while self.prod.dataprodover==False:
            sleep(0.1)
            #display the conternt of list when dataproduct is over
            #print(self.prod.lst)
        print('Item consumed',self.prod.lst)
#create producer object
p=Producer()
#create consumer object
c=Consumer(p)
t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()




            
