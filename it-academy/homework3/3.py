m = input('m = ')
n = input('n = ')
result = {}
for number in xrange(m, n+1):
    result[number] = ''
    for den in xrange(2, number-1):
        if number % den == 0:
            result[number] += '{0} '.format(den)
for key in sorted(result):
    print '{0}: {1}'.format(key, result[key])
