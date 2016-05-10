import requests
import json
import sys
import operator
import collections

client_id = 'b64010a8ea3c37918237'
client_secret = '1aabe583e1fa6f011a264a04012d1c01'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

d = collections.defaultdict(list)
lines = [
    "53164f4bcd530e1ae90000f5",
    "52d4a2479c18db3c5d00036d",
    "4df3ce2bd85a53000100243b",
    "542e86e47261695773da1700",
    "52840714275b2442c8000150",
    "4e96f70a6e481d0001002c73",
    "516df2b89ad2d38886001378",
    "515b34a9223afaab8f000905",
    "53ee751c6361721944780200",
    "4e96f7596e481d0001002cf3",
    "53393f7a275b2458b10004a9",
    "505fa4d3e22288000200007d",
    "5458e1467261696efe210700",
    "4d8b929c4eb68a1b2c0002e4",
    "5324d4657622dd48700001e3"
]
# for line in sys.stdin:
for line in lines:
    line = line.rstrip()
    api_url = "https://api.artsy.net/api/artists/{}".format(line)

    # инициируем запрос с заголовком
    r = requests.get(api_url, headers=headers)
    r.encoding = "utf-8"
    # разбираем ответ сервера
    j = json.loads(r.text)
    d[j["birthday"]].append(j["sortable_name"])
for year in sorted(d):
    print(str(d[year]))
