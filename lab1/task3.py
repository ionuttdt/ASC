"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""

from threading import Semaphore, Thread
from random import randint, seed
from time import sleep

SIZE = ["small", "medium", "big"]
TYPE = ["nice", "strong", "italiano"]

class Coffee:
    """ Base class """
    def __init__(self):
        pass

    def get_name(self):
        """ Returns the coffee name """
        raise NotImplementedError

    def get_size(self):
        """ Returns the coffee size """
        raise NotImplementedError


class ExampleCoffee:
    """ Espresso implementation """
    def __init__(self, size):
        pass

    def get_message(self):
        """ Output message """
        raise NotImplementedError


class Espresso(Coffee):
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def get_message(self):
        return f"type: {self.type}, size: {self.size} espresso"


class Americano(Coffee):
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def get_message(self):
        return f"type: {self.type}, size: {self.size} americano"


class Cappuccino(Coffee):
    def __init__(self, size, type):
        self.size = size
        self.type = type

    def get_message(self):
        return f"type: {self.type}, size: {self.size} cappuccino"


class Distributor:
    def __init__(self, size):
        self.buff = []
        self.size = size
        self.gol = Semaphore(value=size)
        self.plin = Semaphore(value=0)

    def put(self, el):

        self.gol.acquire()
        self.buff.append(el)
        sleep(randint(1, 3))
        self.plin.release()

    def get(self):
        self.plin.acquire()
        elem =  self.buff.pop()
        self.gol.release()

        return elem


class User(Thread):
    def __init__(self, id, distr):
        Thread.__init__(self)
        self.id = id
        self.distr = distr


    def consume(self, distr):


        print(f" User {self.id} consumed {distr.get().get_message()}")



    def run(self):
        while True:
            self.consume(self.distr)


class CoffeeF(Thread):
    def __init__(self, id, distr):
        Thread.__init__(self)
        self.id = id
        self.distr = distr


    def make(self, distr):

        #distr.put()
        t = randint(0, 2)
        i = randint(0, 2)
        j = randint(0, 2)

        if t == 0:
            c = Espresso(SIZE[i], TYPE[j])
        elif t == 1:
            c = Americano(SIZE[i], TYPE[j])
        else:
            c = Cappuccino(SIZE[i], TYPE[j])

        self.distr.put(c)
        print(f" Factory {self.id} produced {c.get_message()}")


    def run(self):
        while True:
            self.make(self.distr)


def main():
    n, nr_prod, nr_cons = map(int, input().split())

    distr = Distributor(n)

    prod_list = []
    cons_list = []
    for i in range(nr_prod):
        prod_list.append(CoffeeF(i, distr))
        prod_list[i].start()
    for i in range(nr_cons):
        cons_list.append(User(i, distr))
        cons_list[i].start()

    for i in range(nr_prod):
        prod_list[i].join()
    for i in range(nr_cons):
        cons_list[i].join()

if __name__ == '__main__':
    seed()
    main()