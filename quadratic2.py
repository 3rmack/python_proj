import cmath
import math
import sys


def get_float(msg, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(msg))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None
        except ValueError as err:
            print(err)
    return x

print("ax\N{SUPERSCRIPT TWO}+bx+с=О")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)
х1 = None
х2 = None
discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    х1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:  # discriminant < 0
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
if b == 0:
    if c == 0:
        equation = ("{0:+}x\N{SUPERSCRIPT TWO}=0"" \N{RIGHTWARDS ARROW} x={1}").format(a, x1)
    else:
        equation = ("{0:+}x\N{SUPERSCRIPT TWO}{1:+}=0"" \N{RIGHTWARDS ARROW} x={2}").format(a, c, x1)
else:
    if c == 0:
        equation = ("{0:+}x\N{SUPERSCRIPT TWO}{1:+}x=0"" \N{RIGHTWARDS ARROW} x={2}").format(a, b, x1)
    else:
        equation = ("{0:+}x\N{SUPERSCRIPT TWO}{1:+}x{2:+}=0"" \N{RIGHTWARDS ARROW} x={3}").format(a, b, c, x1)
if x2 is not None:
    equation += " or x={0}". format(x2)
print(equation)
