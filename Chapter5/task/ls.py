import os
import time
import datetime
from optparse import OptionParser


options = OptionParser()
options.add_option("-H", "--hidden", help="show hidden files [default: off]",
                   action="store_true", default="False")
options.add_option("-m", "--modified", help="show last modified date/time [default: off]",
                   action="store_true", default="False")
options.add_option("-o", "--order", help="order by ('name', 'n', 'modified', 'm', 'size', 's') [default: name]",
                   default="name")
options.add_option("-r", "--recursive", help="recurse into subdirectories [default: off]",
                   action="store_true", default="False")
options.add_option("-s", "--size", help="show sizes [default: off]",
                   action="store_true", default="False")
opts, args = options.parse_args()
print(opts)
#print(args)


result = dict()


def get_stat(item, path):
    file = os.path.join(path, item)
    item_size = os.path.getsize(file)
    item_ctime = os.path.getctime(file)
    item_mtime = os.path.getmtime(file)
    if os.path.isdir(file):
        result[file] = [time.ctime(item_ctime), time.ctime(item_mtime), 0, item+"\\"]
    else:
        result[file] = [time.ctime(item_ctime), time.ctime(item_mtime), item_size, item]


def sort(result):
    if opts.order in ["n", "name"]:
        sort_by = 3  # сортировка по указанному ключу списка
    elif opts.order in ["size", "s"]:
        sort_by = 2
    elif opts.order in ["modified", "m"]:
        sort_by = 1
    result_sorted = sorted(result.items(), key=lambda e: e[1][sort_by])
    return result_sorted


def print_result(result):
    c = 0
    m = 1
    s = 2
    n = 3
    for dir in result:
        created = dir[1][c]
        modified = dir[1][m]
        size = dir[1][s]
        name = dir[1][n]
        if opts.modified is not True:
            modified = ""
        if opts.size is not True:
            size = ""
        if name.endswith("\\"):
            size = "DIR"
        print("{0: ^.30}   {1: ^.30}   {2: >10}   {3:<80}".format(created, modified, size, name))


if opts.recursive is True:
    for stack in os.walk(args[0]):
        for subdir in stack[1]:
            get_stat(subdir, stack[0])
        for filename in stack[2]:
            get_stat(filename, stack[0])
else:
    for item in os.listdir(args[0]):
        get_stat(item, args[0])

result_sorted = sort(result)

# for d1 in result:
#     print(d1)
# for d2 in result_sorted:
#     print(d2)

# print(result)

# print(result_sorted)
print_result(result_sorted)
