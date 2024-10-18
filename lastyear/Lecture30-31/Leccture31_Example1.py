'''
#creating a Thread without using a class
from threading import *
#create a function
def display():
    print('Hello I am running \n')
    
#create a thread and run the function for 5 times
for i in range(5):
    #create the thread and specify the function as its target
    t=Thread(target=display)
    #run the thread
    
    #t.start()
'''
#Style2
#creating a class without using a class
from threading import *
#create a function
def display(str):
    print(str)
    
    
#create a thread and run the function for 5 times
for i in range(5):
    #create the thread and specify the function as its target
    t=Thread(target=display,args=('Hello,I am running \n',))
    #run the thread
    
    #t.start()

