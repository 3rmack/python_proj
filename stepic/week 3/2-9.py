import re
import sys


lines = ["attractionnn", "buzzzz", "tut"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"((\w)\2+)"
    repl = r"\2"
    answers.append(re.sub(pattern, repl, line))
for answer in answers:
    print(answer)
