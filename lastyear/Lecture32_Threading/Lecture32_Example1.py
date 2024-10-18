#Credit: https://www.pythontutorial.net/advanced-python/python-threading-lock/

from threading import Thread
from time import sleep

counter = 0

def increase(by):
    global counter

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'main function counter={counter} \n')


# create threads
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
#print(f'The final counter1 is {counter}')
t2.join()
print(f'The final counter is {counter}')


