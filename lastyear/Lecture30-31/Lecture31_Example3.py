#python program to create a thread by making our class as sub class to Thread class
#creating our own class
from threading import Thread
#create a class as sub clas to Thread class
class MyThread(Thread):
    #overide the run method of Thread class
    def __init__(self,str):
        Thread.__init__(self)
        self.str=str
    
    def run(self):
        for i in range(1,6):
            print(self.str)
            
#create an instance of MyThread class
t1=MyThread('Hello')
#start running the thread t1
print('Thread is starting \n')
t1.start()
#wait till thread completes execution
t1.join()
print('complete the execution')
