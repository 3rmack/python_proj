import requests
import re

# content = requests.get("﻿https://stepic.org/media/attachments/lesson/24471/02/﻿")
# url_results = set()
# pattern1 = r'a href=[\'"]?([^\'" >]+)'
# # pattern1 = r'a href=[\'"]((ftp:\/\/)?|(http:\/\/)?|(https:\/\/))(\w+\.+\w+(\.\w+)?)'
# links = re.findall(pattern1, content.text)
# # print(links)
# pattern2 = r'(\w+\.+\w+(\.\w+)?)'
# for link in links:
#     match = re.search(pattern2, link)
#     if match:
#         # print(match.group())
#         url_results.add(match.group())
# # print()
# for url in sorted(url_results):
#     print(url)


urls_test = ["<a href=\"http://stepic.org/courses\">", "<a href=\'https://stepic.org\'>",
        "<a href=\'http://neerc.ifmo.ru:1345\'>", "<a href=\"ftp://mail.ru/distib\" >",
        "<a href=\"ya.ru\">", "<a href=\"www.ya.ru\">", "<a href=\"../skip_relative_links\">"]

# content = requests.get("﻿https://tut.by")
url_results = []

pattern1 = r'a href=[\'"]?([^\'" >]+)'
for url in urls_test:
    link = re.findall(pattern1, url)
    url_results += link

domains_result = []
pattern2 = r'(\w+\.+\w+(\.\w+)?)'
result = set()
for url2 in url_results:
    domain = re.search(pattern2, url2)
    if domain:
        result.add(domain.group())

for res in sorted(result):
    print(res)
