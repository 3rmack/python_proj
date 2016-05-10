import re
import sys


lines = ["There’ll be no more \"Aaaaaaaaaaaaaaa\"", "AaAaAaA AaAaAaA"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b[Aa]+\b"
    repl = r"argh"
    answers.append(re.sub(pattern, repl, line, count=1))
for answer in answers:
    print(answer)
