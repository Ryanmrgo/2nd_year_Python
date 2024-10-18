
from threading import Thread, Lock
from time import sleep

class TaskManager:
    def __init__(self):
       self.s=input("You input string:")
       self.l = Lock() # Create a lock object

    def task1(self):
        self.l.acquire() # Lock the current object
        #s="Today is April Fool Day."
        print(self.s.upper())
        sleep(2) # Simulating the time taken for task1
        print("Task1: Done ")
        self.l.release() # Release the lock

    def task2(self):
        self.l.acquire()# Lock the current object
        #s="Today is April Fool Day."
        print(self.s.lower())
        sleep(2) # Simulating the time taken for task2
        print("Task2: Done ")
        self.l.release() # Release the lock

# Create an instance of TaskManager


manager = TaskManager()
# Create threads for task1 and task2
thread1 = Thread(target=manager.task1)
thread2 = Thread(target=manager.task2)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()