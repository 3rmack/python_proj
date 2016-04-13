import os
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
#print(type(opts))
#print(opts.recursive)
#print(args)
if opts.recursive is True:
    for item in os.walk(args[0]):
        print(item)
        #print(item.st_size)
else:
    for item in os.listdir(args[0]):
        if os.path.isdir(args[0]+"\\"+item):
            print("'{0}' is directory".format(item))
        else:
            print(os.stat(args[0]+"\\"+item))
