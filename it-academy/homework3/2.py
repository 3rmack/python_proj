# coding: utf-8
from __future__ import division  # вычитал на stackoverflow, реализует деление как в 3.5
while True:
    x = input('x = ')
    y = input('y = ')
    sign = raw_input('sign: ')
    if sign in ['+', '-', '/', '*']:
        if sign == '+':
            print 'z =', x + y
        elif sign == '-':
            print 'z =', x - y
        elif sign == '/':
            if y == 0:
                print 'Division by zero error'
            else:
                print 'z =', x / y
        elif sign == '*':
            print 'z =', x * y
    elif sign == '0':
        break
    else:
        print 'Sign is incorrect'
