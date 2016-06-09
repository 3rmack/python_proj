# coding: utf-8
n = input('n: ')
factorial = 1
for i in xrange(n):
    factorial *= i + 1
try:
    if factorial % 2 == 0:
        raise Exception('Четный результат')
except Exception as err:
    print err.message
