#python program to create a thread by making our class as sub class to Thread class
#creating our own class
from threading import Thread
#create a class as sub clas to Thread class
class MyThread(Thread):
    #overide the run method of Thread class
    def run(self):
        for i in range(1,6):
            print(i)
            
#create an instance of MyThread class
t1=MyThread()
#start running the thread t1
#print('Thread is starting \n')
t1.start()
#wait till thread completes execution
t1.join()
#print('complete the execution')
'''
t2=MyThread()
#start running the thread t1
#print('Thread is starting \n')
t2.start()
#wait till thread completes execution
t2.join()
'''


