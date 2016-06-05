# coding: utf-8
with open('in.txt') as file_in:
    file_in_lines = file_in.readlines()
data = file_in_lines[0].split()
k = 0  # левая граница среза
i = 0  # правая граница среза
sample_line = '-'*31
sample_string = '| {0:^3} | {1:^3} | {2:^3} | {3:^3} | {4:^3} |'  # сэмпл строки для записи в out.txt
result = {}  # словарь со строками, которые буду записываться в out.txt
while i <= len(data):  # обходим исходный список срезами по 5 элементов
    i += 5  # увеличиваем правую границу среза
    print(sample_line)  # первая стройка, печатаю на экран для проверки
    if len(data[k:i]) == 5:  # если длина среа равна 5, значит можно формировать строку для вывода
        print(sample_string.format(*data[k:i]))  # печатаю на экран для проверки
        result[i] = sample_string.format(*data[k:i]) + '\n'  # добавление в словарь выходной строки
    else:
        last_string = data[k:i]
        while len(last_string) < 5:  # если длина среза меньше 5, то нужно добавить в список элементы в виде пустых строк
            last_string.append('')
        print(sample_string.format(*last_string))   # печатаю на экран для проверки
        result[i] = sample_string.format(*last_string) + '\n'  # добавление в словарь выходной строки
    k += 5  # увеличиваем левую границу среза
print(sample_line)
# print(sorted(result))
with open('out.txt', 'w') as file_out:
    for line in sorted(result):
        file_out.write(sample_line + '\n')
        file_out.write(result[line])
    file_out.write(sample_line + '\n')
