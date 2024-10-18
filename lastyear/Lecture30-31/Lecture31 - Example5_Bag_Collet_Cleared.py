# CSE 2040 - Lecture 31 - Example 5

# Illustrating synchronization cleaning and clearing the basket
# But does not synchronize well - Why?

from threading import Thread, current_thread
from time import time, sleep
from random import randint

# Leader of the worker group is the main thread
bags_collected = 0
bags_cleared = 0
workers = []
start_time = 0

# Fucntion to clear the content of the basket
def clearBasket():
    global bags_collected
    global bags_cleared
    global start_time
    print(current_thread().name + " is clearing the basket" + "\n",end="")
    while time() - start_time <= 25:
        worker_clears = randint(5,20)
        bags_cleared = bags_cleared + worker_clears
        sleep(randint(1,5))
    print(current_thread().name + " has finished clearing the basket" + "\n",end="")
     
# Function to count the plastic bags collected by the workers
def collectBags():
     global bags_collected
     global start_time
     print(current_thread().name + " has started cleaning" + "\n",end="")
     while time() - start_time <= 20:
         worker_collects = randint(5,20)
         bags_collected = bags_collected + worker_collects
         sleep(randint(1,5))
     print(current_thread().name + " has finished cleaning" + "\n",end="")

# Creating worker threads
for i in range(1,16):
    if i <= 10:
        worker = Thread(target=collectBags, name="Worker " + str(i))
    else:
        worker = Thread(target=clearBasket, name="Worker " + str(i))
    workers.append(worker)
     
# Leader of the worker group keeping track of bags collected
print()
print("Cleaning of park starts now!")
start_time = time()
print()
print("Cleaning in progress ...")
print()

start_time = time()
# Start the cleaning process
for worker in workers:
     worker.start()
print()

# Threads joining after work completion
for worker in workers:
    #print(worker.name + " has joined the main thread" + "\n",end="")
    worker.join()

print()
print("Cleaning and clearing are completed!")
print()
print("Bags collected " + str(bags_collected))
print("Bags cleared " + str(bags_cleared))
print("Bags remaining " + str(bags_collected - bags_cleared))

