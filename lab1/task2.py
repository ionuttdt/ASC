"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""

from random import randint, seed
from threading import Thread
import sys

# n = input()
# try:
#     n = int(n)
# except ValueError:
#     print("ERROR")
#     exit(-1)

n = sys.argv[1]
try:
    n = int(n)
except ValueError:
    print("ValueError")
    exit(-1)

def func(id, nr):
    #print("Hello, I'm Thread-",id ,"and I received the number", nr)
    print(f"Hello, I'm Thread-{id} and I received the number {nr}")


thread_list = []
seed()

for i in range(n):
    thread = Thread(target=func, args=(i, randint(0, 100)))
    thread.start()
    thread_list.append(thread)

for i in range(len(thread_list)):
    thread_list[i].join()

