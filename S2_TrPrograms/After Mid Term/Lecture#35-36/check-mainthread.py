#Python program to find the currently running thread in a python program.

import threading

print('Let us find the current thread')

print('Currently running thread:')
print(threading.current_thread().getName())

