from threading import Thread, current_thread
from time import sleep

class Railway:
    # Constructor that accepts the number of available berths
    def __init__(self, available):
        self.available = available

    # A method that reserves a berth
    def reserve(self, wanted):
        # Display the number of available berths
        print('Available no. of berths =', self.available)

        # Acquire the lock to ensure only one thread can access this block at a time
        if self.available >= wanted:
            self.available -= wanted  # Decrease the number of available berths
            # Find the thread name
            name = current_thread().getName()
            # Display berth is allotted for the person
            print('%d berth(s) allotted for %s' % (wanted, name))
            # Make a time delay to simulate the reservation process
            sleep(1.5)
        else:
            print('Sorry, no berth(s) are allotted')

# Create an instance of the Railway class with 1 available berth
obj = Railway(5)

# Create two threads and specify 1 berth is needed for each
t1 = Thread(target=obj.reserve, args=(3,))
t2 = Thread(target=obj.reserve, args=(2,))

# Give names to threads
t1.setName('First Person')
t2.setName('Second Person')

# Run the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print('Both threads have finished')
