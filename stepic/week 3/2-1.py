import re
import sys


lines = ["catcat", "cat and cat", "catac", "cat", "ccaatt", "..cacat \.?%catcat0"]
answers = []
for line in lines:
# for line in sys.stdin:
    line = line.rstrip()
    pattern = r"(.*cat.*){2,}"
    # print(re.search(pattern, line))
    if re.search(pattern, line):
        # print(line)
        answers.append(line)
for answer in answers:
    print(answer)
