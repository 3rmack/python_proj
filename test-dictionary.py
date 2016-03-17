d1 = dict(a=1, b=2, c=3)
d2 = dict(d=4, e=5, f=6)
d3 = [7, 8, 9]

# print(d1)
# print(d2)
# for i, v in d1.items():
#     print("key="+i, "value="+str(v))
#
# for i in d1.items():
#     print(i)
#     print(type(i))

for key in d1.keys():
    d1[key] += 1
print(d1)

#d3 = (10, 11, 12)
d4 = d1.fromkeys(d1)
#print(d4)