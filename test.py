import re
pattern = "spama"
source = r"spamspamadffspama"
g = re.search(pattern, source)
if g:
    print (g.group())

#print(g)
if re.match(pattern, source):
    print("match")
else:
    print("fuckoff!")

if re.search(pattern, source):
    print("match")
else:
    print("fuckoff!")

print(re.findall(pattern, source))
