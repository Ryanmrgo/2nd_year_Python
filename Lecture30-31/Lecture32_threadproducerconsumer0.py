import threading
import time

# Create producer class
class Producer:
    def __init__(self):
        self.lst = []

    def produce(self):
        # Create 1 to 10 items
        for i in range(1, 11):
            self.lst.append(i)
            time.sleep(0.5)
            print('Item produced')

class Consumer:
    def __init__(self, prod):
        self.prod = prod

    def consume(self):
        while True:
            if len(self.prod.lst) == 10:
                # Display the content of the list when data production is over
                print('Item consumed',self.prod.lst)
                break
            time.sleep(0.2)

# Create producer object
p = Producer()
# Create consumer object
c = Consumer(p)

# Create threads
t1 = threading.Thread(target=p.produce)
t2 = threading.Thread(target=c.consume)

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
