import os
import time
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
# print(opts)
# print(args)


result = dict()


def get_stat(item, path):
    file = os.path.join(path, item)
    item_size = os.path.getsize(file)
    item_ctime = os.path.getctime(file)
    item_mtime = os.path.getmtime(file)
    if os.path.isdir(file):
        result[file] = [time.ctime(item_ctime), time.ctime(item_mtime), "", file+"\\"]
    else:
        result[file] = [time.ctime(item_ctime), time.ctime(item_mtime), item_size, file]


def print_result(result):
    if opts.modified is True:
        if opts.size is True:
            print("{0:-^30.35} {1:-^30.35} {2:-^10} {3:-^80}".format("Created", "Modified", "Size", "Filename"))
            for result_item in result:
                print("{0:^30.35} {1:^30.35} {2:>10} {3:<80}".format(result[result_item][0], result[result_item][1],
                                                                     result[result_item][2], result[result_item][3]))
        else:
            print("{0:-^30.35} {1:-^30.35} {2:-^80}".format("Created", "Modified", "Filename"))
            for result_item in result:
                print("{0:^30.35} {1:^30.35} {2:<80}".format(result[result_item][0], result[result_item][1],
                                                             result[result_item][3]))
    else:
        if opts.size is True:
            print("{0:-^30.35} {1:-^10} {2:-^80}".format("Created", "Size", "Filename"))
            for result_item in result:
                print("{0:^30.35} {1:^10} {2:<80}".format(result[result_item][0], result[result_item][2],
                                                          result[result_item][3]))
        else:
            print("{0:-^30.35} {1:-^80}".format("Created", "Filename"))
            for result_item in result:
                print("{0:^30.35} {1:<80}".format(result[result_item][0], result[result_item][3]))


if opts.recursive is True:
    for stack in os.walk(args[0]):
        for subdir in stack[1]:
            get_stat(subdir, stack[0])
        for filename in stack[2]:
            get_stat(filename, stack[0])
        # print(item)
        # get_stat(item)
else:
    for item in os.listdir(args[0]):
        get_stat(item, args[0])
# print(result)
print_result(result)
