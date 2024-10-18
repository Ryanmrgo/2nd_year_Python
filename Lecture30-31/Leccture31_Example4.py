#creating a thread without making sub class to Thread class

from threading import *
#create own class
class MyThread:
    #a constructor
    def __init__(self,str):
        self.str=str
    # a method
    def display(self,x,y):
        print(current_thread().getName())
        #self.str=str
        print(self.str)
        print('The ages are',x,y)
#create an instance to our class and store 'Hello'
obj=MyThread('hello thread1')
#obj='hh'
#create a thread to run display method of obj
t1=Thread(target=obj.display,args=(1,2))
#run the thread
print('Thread1 is starting')
t1.start()
obj2=MyThread('hello thread2')
#obj='hh'
#create a thread to run display method of obj
t2=Thread(target=obj2.display,args=(1,2))
#run the thread
print('Thread2 is starting')
t2.start()

# importing thread module
from threading import *
  
# class does not extend thread class
class MyThread:
    def display(self):
        i = 0
        print(current_thread().getName())
        while(i <= 10):
            print(i)
            i = i + 1
  
# creating object of out class
print('creating object')
obj = MyThread()
  
# creating thread object
print('creating thread object')
t = Thread(target = obj.display)
print('invoking thread ')
# invoking thread
t.start()


