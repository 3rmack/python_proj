n = 15
first = 3
fib = [first, first]
for i in range(2, n):
    fib.append(fib[i-2] + fib[i-1])
print(fib)
