n = raw_input('Enter number: ')
sum = 0
mult = 1
for i in n:
    sum += int(i)
    mult *= int(i)
print 'sum =', sum, '\n', 'multiplication =', mult
