import sys
import unicodedata


words = None


def print_unicode_table(words):
    print("decimal  hex  chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))
    code = ord(" ")
    end = sys.maxunicode
    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if words is None or words in name.lower():
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        code += 1


if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        words = 0
    else:
        words = sys.argv[1:].lower()
if words != 0:
    print_unicode_table(words)
