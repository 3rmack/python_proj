f = open("test1.txt")
for line in f:
    line = line.rstrip()
    print(line)

f.close()