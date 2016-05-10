import re
import sys


lines = ["zabcz", "zzz", "zzxzz", "zz", "zxz", "zzxzxxz"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"z\w{3}z"
    # print(re.search(pattern, line))
    if re.search(pattern, line):
        # print(line)
        answers.append(line)
for answer in answers:
    print(answer)