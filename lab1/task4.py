from threading import Thread
import threading
from time import sleep
from random import randint, seed


class Filozof(Thread):

    def __init__(self, id, buff):
        Thread.__init__(self)
        self.id = id
        self.buff = buff

    def run(self):
        if id == 0:
            self.buff[0].acquire()
            self.buff[len(self.buff) - 1].acquire()
        else:
            self.buff[self.id].acquire()
            self.buff[self.id - 1].acquire()

        print(f"filozof {self.id}")
        sleep(randint(1, 2))

        if self.id == 0:
            self.buff[0].release()
            self.buff[len(self.buff) - 1].release()
        else:
            self.buff[self.id].release()
            self.buff[self.id - 1].release()


def main():
    n = int(input())
    buff = []
    for i in range(n):
        lock = threading.Lock()
        buff.append(lock)

    list = []
    for i in range(n):
        list.append(Filozof(i, buff))
        list[i].start()
    for fil in list:
        fil.join()

if __name__ == "__main__":
    seed()
    main()