#python program to show single tasking
from threading import *
from time import *
#create our own class
class MyThread:
    #a method that performs 3 tasks
    def prepareTea(self):
        self.task1()
        self.task2()
        self.task3()
    def task1(self):
        print('Boil Milk and teapowder for 5 minutes....',end='')
        sleep(5)
        print('Task1 Done')
    def task2(self):
         print('Add Sugar and Boil for 3minutes....',end='')
         sleep(3)
         print('Task2 Done')
    def task3(self):
        print('Filter it and serve....',end='')
       # sleep(3)
        print('Task3 Done')
#create an instance to our class
obj=MyThread()
#create a thread and run prepareTea method of obj
t=Thread(target=obj.prepareTea)
print('Single Tasking is started')
t.start()
