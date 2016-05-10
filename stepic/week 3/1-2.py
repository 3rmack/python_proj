s = "aaaaa"
t = "a"
sindex = 0
count = 0


def count_func(s, t, sindex, count):
    if t in s:
        try:
            sindex = s.index(t, sindex) + 1
            count += 1
            count = count_func(s, t, sindex, count)
        except ValueError:
            return count
    return count


print(count_func(s, t, sindex, count))
