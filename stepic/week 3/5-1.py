import requests
import sys

# number = input("Number? ")
for line in sys.stdin:
    line = line.rstrip()
    api_url = "http://numbersapi.com/{}".format(line)
    params = {
        "json": "text",
        "type": "math"
    }
    res = requests.get(api_url, params=params)
    data = res.json()
    # print(data)
    if data["found"]:
        print("Interesting")
    else:
        print("Boring")
