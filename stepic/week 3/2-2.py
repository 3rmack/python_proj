import re
import sys


lines = ["cat", "catapult and cat", "catcat", "concat", "Cat", "\"cat\"", "!cat?"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\bcat\b"
    # print(re.search(pattern, line))
    if re.search(pattern, line):
        # print(line)
        answers.append(line)
for answer in answers:
    print(answer)