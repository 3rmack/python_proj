import re
import sys


lines = ["I need to understand the human mind", "humanity"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"human"
    repl = r"computer"
    answers.append(re.sub(pattern, repl, line))
for answer in answers:
    print(answer)