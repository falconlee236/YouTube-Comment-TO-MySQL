from bs4 import BeautifulSoup
import requests as rq
from sys import exit

url = "https://youtu.be/PV1gCvzpSy0"  # 방탄소년단

res = rq.get(url)
if res.status_code != 200:
    print("Fail")
    exit()

soup = BeautifulSoup(res.content, "html.parser")
print(res.content)

a = {}
a['hello'] = 1
print(a['hello'])

