import re
import sys


lines = ["this is a text", "\"this' !is. ?n1ce,"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b([\w])([\w])(\w*)\b"
    repl = r"\2\1\3"
    answers.append(re.sub(pattern, repl, line))
for answer in answers:
    print(answer)
