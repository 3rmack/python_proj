objects = [1,2,1,4,5,4,3]
ans = 0
id_dict = dict()
for obj in objects:
    print(id(obj))
    id_dict[id(obj)] = obj
print(len(id_dict))