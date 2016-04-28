import itertools


def primes():
    p = 2
    while True:
        i = p
        n = 0
        while i > 0:
            if p % i == 0:
                n += 1
            i -= 1
        if n == 2:
            yield(p)
        p += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]