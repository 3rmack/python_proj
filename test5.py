import sys
# args = sys.argv  # получаем list аргументов
# #print(args)
# maxwidtharg = 100  # задаем дефолтное значение
# formatarg = ".0f"  # задаем дефолтное значение
# if len(args) > 1:
#     for arg in args[1:]:  # обрабатываем каждый аргумент из list
#         print(arg)
#         i = None
#         i = arg.find("format")  # ищем вхождение строки "format" в аргументе, получаем индекс (позицию) первого вхождения
#         #print(i)
#         if i == 0:  # если индекс (позиция) первого вхождения равна нулю - воспринимаем это как параметр и парсим строк далее
#             u = arg.find("=")  # ищем символ "=", все что после него воспринимаем как аргумент
#             formatarg = str((arg[u+1:]))  # присваиваем аргумент переменной для последующего вывода
#             print(formatarg)
#             print(type(formatarg))
#         i = arg.find("maxwidth")  # ищем вхождение строки "maxwidth" в аргументе, получаем индекс (позицию) первого вхождения
#         if i == 0:  # если индекс (позиция) первого вхождения равна нулю - воспринимаем это как параметр и парсим строк далее
#             u = arg.find("=")  # ищем символ "=", все что после него воспринимаем как аргумент
#             maxwidtharg = int((arg[u+1:]))  # присваиваем аргумент переменной для последующего вывода
#             print(maxwidtharg)
#             print(type(maxwidtharg))
# options = (maxwidtharg, formatarg)  # создаем tuple с полученными аргументами
# print(options)
# print(type(options))


def process_options():
    maxwidtharg = 100  # задаем дефолтное значение
    formatarg = ".0f"  # задаем дефолтное значение
    msg = (
        "usage:\n"
        "csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html\n"
        "maxwidth is an optional integer; if specified, it sets the maximum number of characters that can be output for string fields,otherwise a default of 100 characters is used\n"
        "format is the format to use for numbers; if not specified it defaults to \".Of\""
        )
    args = sys.argv  # получаем list аргументов
    if args[1] in ("-h", "--help"):
        print(msg)
        options = (None, None)
        return options
        #sys.exit(0)
    if len(args) > 1:
        for arg in args[1:]:  # обрабатываем каждый аргумент из list
            i = arg.find("format")  # ищем вхождение строки "format" в аргументе, получаем индекс (позицию) первого вхождения
            if i == 0:  # если индекс (позиция) первого вхождения равна нулю - воспринимаем это как параметр и парсим строк далее
                u = arg.find("=")  # ищем символ "=", все что после него воспринимаем как аргумент
                formatarg = str((arg[u+1:]))  # присваиваем аргумент переменной для последующего вывода
                i = u = -1  # сбрасываем индексы
            i = arg.find("maxwidth")  # ищем вхождение строки "maxwidth" в аргументе, получаем индекс (позицию) первого вхождения
            if i == 0:  # если индекс (позиция) первого вхождения равна нулю - воспринимаем это как параметр и парсим строк далее
                u = arg.find("=")  # ищем символ "=", все что после него воспринимаем как аргумент
                maxwidtharg = int((arg[u+1:]))  # присваиваем аргумент переменной для последующего вывода
                i = u = -1  # сбрасываем индексы
    options = (maxwidtharg, formatarg)  # создаем tuple с полученными аргументами
    return options
options = process_options()
if options[0] == options[1] == None:
    sys.exit()
print(options)
maxwidth = options[0]
print(maxwidth)
