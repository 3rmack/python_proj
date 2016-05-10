import re
import sys


lines = ["\w denotes word character", "No slashes here"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"[\\]\w*"
    # print(re.search(pattern, line))
    if re.search(pattern, line):
        # print(line)
        answers.append(line)
for answer in answers:
    print(answer)