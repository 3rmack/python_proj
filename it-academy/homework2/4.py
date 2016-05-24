my_list = [1, 2, 3, 4, 5, 10, 7]
new_list = my_list[:]
for i in range(len(my_list)):
    new_list[i-1] = my_list[i]
print(new_list)
