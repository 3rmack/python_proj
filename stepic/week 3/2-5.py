import re
import sys


lines = ["blabla is a tandem repetition", "123123 is good too", "go go", "aaa"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b(\w+)\1\b"
    # print(re.search(pattern, line))
    if re.search(pattern, line):
        # print(line)
        answers.append(line)
for answer in answers:
    print(answer)