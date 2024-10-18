import threading
import time

def worker(name):
    for i in range(5):
        print(f"Thread {name}: Working {i + 1}...")
        time.sleep(1)

# Create two threads with different names
thread1 = threading.Thread(target=worker, args=("Thread-1",))
thread2 = threading.Thread(target=worker, args=("Thread-2",))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish (optional)
thread1.join()
thread2.join()

print("All threads finished.")
