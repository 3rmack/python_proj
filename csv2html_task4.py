import sys
from xml.sax.saxutils import escape


def main():
    options = process_options()
    if options[0] == options[1] == None:
        sys.exit()
    maxwidth = options[0]
    format1 = options[1]
    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "green"
            elif count % 2:
                color = "white"
            else:
                color = "yellow"
            print_line(line, color, maxwidth, format1)
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_end():
    print("</table>")


def print_line(line, color, maxwidth, format1):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:1}</td>".format(x, format1))
                #print("<td align='right'>{0:1}</td>".format(round(x), format1))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = escape(field)
                #field = escape_html(field)
                if len(field) <= maxwidth:
                    print("<td>{0}</td>".format(field))
                else:
                    print("<td>{0:.{1}} ...</td>".format(field, maxwidth))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # начало строки в кавычках
                quote = c
            elif quote == c:  # конец строки в кавычках
                quote = None
            else:
                field += c  # другая кавычка внутри строки в кавычках
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c  # добавить символ в поле
    if field:
        fields.append(field)  # добавить последнее поле в список
    return fields


# def escape_html(text):
#     text = text.replace("&", "&amp;")
#     text = text.replace("<", "&lt;")
#     text = text.replace(">", "&gt;")
#     return text


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


main()
