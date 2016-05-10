s = "abbb"
a = "ab"
b = "a"
i = 0


def rep(s, a, b, i):
    if a not in s:
        # print("no")
        return i
    elif a in s and a not in b:
        # print("yes")
        s = s.replace(a, b)
        i += 1
        # print(i)
        i = rep(s, a, b, i)
        # print("ss")
        return i
    else:
        return "Impossible"


print(rep(s, a, b, i))
