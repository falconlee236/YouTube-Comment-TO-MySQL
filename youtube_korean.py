# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display
import time
import re


def isHangul(text):
    hancount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
    return hancount > 0

# 웹 드라이버 실행
driver = wd.Chrome(executable_path="chromedriver.exe")
url = "https://www.youtube.com/watch?v=LmApDbvNCXg"
driver.get(url)

# execute_script = 자바스크립트 코드를 실행한다
# execute_script('스크립트', '파라미터')
# 스크립트 부분에 return 스크립트를 이용하면 리턴값을 받을 수 있다
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source
driver.close()

soup = BeautifulSoup(html_source, 'lxml')
youtube_users = []
youtube_comments = []
users = []
comments = []
youtube_users = soup.select("div#header-author > a > span")

for user in youtube_users:
    user = str(user)
    user = user.replace('\n', '')
    user = user.replace('                ', '')
    user = user.replace('              ', '')
    user = user.split(">")
    user = user[1].split("<")
    users.append(user[0])

youtube_comments = soup.select("yt-formatted-string#content-text")

for comment in youtube_comments:
    comment = str(comment.text)
    comment = comment.replace("\n", '')
    comments.append(comment)

print(users)
print(comments)

pd_data = {"ID": users, "Comment": comments}
youtube_pd = pd.DataFrame(pd_data)
display(youtube_pd)

'''
for x, y in zip(comments, users):
    if isHangul(x) is False:
        comments.remove(x)
        users.remove(y)

print(users)
print(comments)
'''


