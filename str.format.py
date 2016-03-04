s = "{0} was {age}. {age} is a good age."
y = s.format("nick", age="25")
print(y)

list = ["one", "two", "three"]
pattern = "1 is {0[0]}, 2 is {0[1]}, 3 = {0[2]}"
str = pattern.format(list)
print(str)

import decimal
print("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("93.4")))
print("{0} {0!s} {0!r} {0!a}".format("dfsdfs"))

movie = "映画のゴジラ"
print("{0!s}".format(movie))
print("{0!r}".format(movie))
print("{0!a}".format(movie))
#print("{0!c}".format(movie))

str2 = "The truth is out there"
print("{0:2^45}".format(str2))

minwidht = 3
maxwidth = 55
print("{0}".format(str2[minwidht:maxwidth]))
print("{0:>{1}.{2}}".format(str2, minwidht, maxwidth))

str3 = 88499392
print("{0:#b} {0:#o} {0:#x} {0:b} {0:o} {0:x}".format(str3))
str4 = -65744.845
print("{0:$>15} {1:*>-20.5e}".format(str3, str4))
str5 = 0xDEFACE
print("{0:#d}".format(str5))

import locale
locale.setlocale(locale.LC_ALL, "")
print("{0:n} $ {1:n}".format(str3, str4))
locale.setlocale(locale.LC_ALL, "C")
print("{0:n} $ {1:n}".format(str3, str4))
#locale.setlocale(locale.LC_ALL, 'en_US')
#print("{0:n} $ {1:n}".format(str3, str4))

import sys
end = sys.maxunicode
print(end)