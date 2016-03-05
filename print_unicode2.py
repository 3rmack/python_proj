import sys
import unicodedata


words = []


def print_unicode_table(words):
    print("decimal  hex  chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))
    code = ord(" ")
    end = sys.maxunicode
    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")  # получаем название символа в str
        namelower = name.lower()  # конвертим все символы в нижний регистр
        namelist = namelower.split()  # конвертим str в list
        #if words is None or words <= namelist:
        if words <= namelist:
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        code += 1


if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        words = 0
    else:
        words = sys.argv[1:]  # получаем list аргументов
        a = 0  # конвертим все элементы list в нижний регистр
        while a < len(words):
            words[a] = words[a].lower()
            a += 1
if words != 0:
    print(words)
    print_unicode_table(words)
