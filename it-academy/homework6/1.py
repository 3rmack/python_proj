from __future__ import division


class Math(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

    def pow(self):
        return self.x ** self.y

    def mod(self):
        return self.x % self.y

m = Math(20, 5)
print m.sum()
print m.sub()
print m.mul()
print m.div()
print m.pow()
print m.mod()
