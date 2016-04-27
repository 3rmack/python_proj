from random import random


class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


# x = RandomIterator(3)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

for x in RandomIterator(10):
    print(x)

class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i - 2], self.lst[self.i - 1]
        else:
            raise StopIteration

class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)

for pair in MyList([1,2,3,4,5]):
    print(pair)