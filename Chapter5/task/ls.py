import os
import time
import locale
from optparse import OptionParser


def parse_optons():
    options = OptionParser()
    options.add_option("-H", "--hidden", help="show hidden files [default: off]",
                       action="store_true", default="False")
    options.add_option("-m", "--modified", help="show last modified date/time [default: off]",
                       action="store_true", default="False")
    options.add_option("-o", "--order", help="order by ('name', 'n', 'modified', 'm', 'created', 'c', 'size', 's') [default: name]",
                       default="name")
    options.add_option("-r", "--recursive", help="recurse into subdirectories [default: off]",
                       action="store_true", default="False")
    options.add_option("-s", "--size", help="show sizes [default: off]",
                       action="store_true", default="False")
    options.add_option("-c", "--created", help="show creation date/time [default: off]",
                       action="store_true", default="False")
    opts, args = options.parse_args()
    # print(opts)
    # print(args)
    return opts, args


def get_stat(result, item, path):
    time_format = "%Y.%m.%d %H:%M:%S"  # задаем формат вывода времени
    file = os.path.join(path, item)  # создаем абсолютный путь до файла, чтобы получить его свойства дальше
    item_size = os.path.getsize(file)  # получаем размер
    item_ctime = time.strftime(time_format, time.gmtime(os.path.getctime(file)))  # получаем время создания
    item_mtime = time.strftime(time_format, time.gmtime(os.path.getmtime(file)))  # получаем время модификации
    # для придания формату времени удобоваримости, передаем получаенное время в "секундах от эпохи" методу time.gtime,
    # который преобразует его в struct_time, а затем передаем struct_time методу time.strftime для вывода времени
    # в нужном нам формате, указанном в начале функции
    if os.path.isdir(file):  # проверяем, является ли элемент директорией
        # если является - добавляет в словаре к его имени backslash и создаем новый элемент словаря
        result[file] = [item_ctime, item_mtime, 0, item+"\\"]
    else:
        # если элемент - файл, то создаем новый элемент словаря
        result[file] = [item_ctime, item_mtime, item_size, item]


def sort(result, opts):
    # определяем по какому элементу сортировать словарь
    if opts.order in ["n", "name"]:
        sort_by = 3  # сортировка по указанному ключу списка
    elif opts.order in ["size", "s"]:
        sort_by = 2
    elif opts.order in ["modified", "m"]:
        sort_by = 1
    elif opts.order in ["created", "c"]:
        sort_by = 0
    # передаем в качестве ключа сортировки элемент из values словаря, определенный выше
    result_sorted = sorted(result.items(), key=lambda e: e[1][sort_by])
    return result_sorted


def print_result(result, opts):
    # т.к. отсортированным мы получаем кортеж, где 1ый эллемент - fq-имя, а второй - список со свойствами, то для
    # упрощения задаем индексы для свойств
    c = 0
    m = 1
    s = 2
    n = 3
    for dir in result:  # обходим все кортежи
        created = dir[1][c]
        modified = dir[1][m]
        size = "{0:n}".format(dir[1][s])  # разбиваем размер на разряды по формату локали
        name = dir[1][n]
        if opts.created is not True:  # опция не включена, не выводим дату создания - записываем в переменную пустую строку
            created = ""
        if opts.modified is not True:  # опция не включена, не выводим дату изменения - записываем в переменную пустую строку
            modified = ""
        if opts.size is not True:  # опция не включена, не выводим размер - записываем в переменную пустую строку
            size = ""
        if name.endswith("\\"):  # если имя заканчивается на слэш (значит эллемент - директория) - меняет размер на DIR
            size = "DIR"
        if opts.hidden is not True:  # не выводим скрытые файлы
            if name.startswith("."):  # проверяем скрыт ли фалй (имя начинается с ".")
                continue
        print("{0: ^.30}   {1: ^.30}   {2: >10}   {3:<80}".format(created, modified, str(size), name))


def main():
    locale.setlocale(locale.LC_ALL, "")
    result = dict()  # словарь для накопления результата обхода все файлов/папок
    opts, args = parse_optons()
    if opts.recursive is True:  # если включен рекурсивный вывод - используем os.walk
        for stack in os.walk(args[0]):  # обходим все корневые пути (1ый эллемент кортежа, возвращаемого os.walk)
            for subdir in stack[1]:  # обходим все имена папок в корневом пути (2ой эллемент кортежа, возвращаемого os.walk)
                get_stat(result, subdir, stack[0])  # вызываем функцию получения свойств папок
            for filename in stack[2]:  # обходим все имена файлов в корневом пути (3ий эллемент кортежа, возвращаемого os.walk)
                get_stat(result, filename, stack[0])  # вызываем функцию получения свойств файлов
    else:  # если рекурсивный вывод не включен - используем os.listdir
        for item in os.listdir(args[0]):
            get_stat(result, item, args[0])
    result_sorted = sort(result, opts)
    # print(result_sorted)
    print()
    print_result(result_sorted, opts)


main()
