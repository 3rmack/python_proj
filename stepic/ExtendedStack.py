class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())
        # операция сложения

    def sub(self):
        self.append(self.pop() - self.pop())
        # операция вычитания

    def mul(self):
        self.append(self.pop() * self.pop())
        # операция умножения

    def div(self):
        self.append(self.pop() // self.pop())
        # операция целочисленного деления


def test():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0

test()