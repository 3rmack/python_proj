import requests
import re

urlA = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
urlB = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
pattern = r"http[s]?:\/\/[\w.\/]*"
result = []

contentA = requests.get(urlA)
urls_in_A = re.findall(pattern, contentA.text)
# print(urls_in_A)
for urlC in urls_in_A:
    contentC = requests.get(urlC)
    url_in_C = re.findall(pattern, contentC.text)
    result += url_in_C
    # print(url_in_C)

if urlB in result:
    print("Yes")
else:
    print("No")
