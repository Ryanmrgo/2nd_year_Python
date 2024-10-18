from threading import Thread, Lock
from time import sleep

class Theatre:
    def __init__(self, str):
        self.str = str
        self.lock = Lock()  # Create a lock for synchronization

    def movieshow(self):
        for i in range(1, 6):
            print('two threads run simultaneously\n')
            print(self.str, ':', i, '\t \t')
            sleep(0.1)

# Create two instances of the Theatre class
obj1 = Theatre('cut tickets\t\t')
obj2 = Theatre('show chair\t\t\t')

# Create two threads to run movieshow
print('Creating two threads')
t1 = Thread(target=obj1.movieshow)
t2 = Thread(target=obj2.movieshow)

print('T1 is started')
t1.start()
print('T2 is started')
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print('Both threads have finished')
