import os
import zipfile

root = os.getcwd()
with zipfile.ZipFile(root + "\main.zip", "r") as zip_ref:
    zip_ref.extractall(".")
result = set()
for i in os.walk("main"):
    print(i)
    for file in i[2]:
        if file.endswith(".py"):
            result.add(i[0])
with open("result2.txt", "w") as result_file:
    for dir in sorted(result):
        result_file.write(dir + "\n")

