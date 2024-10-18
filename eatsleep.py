import threading
import time

# Define a lock
lock = threading.Lock()

# Define a function for Task 1 (eating)
def eat(food):
    global lock
    # Acquire the lock before performing the task
    lock.acquire()
    print("Task 1 (eating): Eating", food)
    time.sleep(2)  # Simulate eating
    # Release the lock after completing the task
    lock.release()

# Define a function for Task 2 (sleeping)
def sleep():
    global lock
    # Acquire the lock before performing the task
    lock.acquire()
    print("Task 2 (sleeping): Sleeping")
    time.sleep(2)  # Simulate sleeping
    # Release the lock after completing the task
    lock.release()

# Create threads for Task 1 and Task 2
thread1 = threading.Thread(target=eat, args=("pizza",))
thread2 = threading.Thread(target=sleep)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Tasks completed")
