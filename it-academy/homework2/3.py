my_dict = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
dict_keys = list(my_dict.keys())  # делаем копию списка ключей, иначе они будут динамически менятся в цикле
for key in dict_keys:
    my_dict[key+str(len(key))] = my_dict.pop(key)
print(my_dict)
