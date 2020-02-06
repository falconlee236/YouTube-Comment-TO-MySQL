# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from bs4 import BeautifulSoup
from IPython.display import display
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import datetime
import time
import re

font_location = "C:\\Users\\user\\Desktop\\python_korean\\스플래툰K[Ver.3.0].ttf"
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc("font", family=font_name)


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

pd_data = {"ID": users, "Comment": comments}
youtube_pd = pd.DataFrame(pd_data)
count_hangul = 0
# 화면 출력 코드
display(youtube_pd)
count_entire = youtube_pd.shape[0]

for x in youtube_pd["Comment"]:
    if isHangul(x) is True:
        count_hangul += 1

count_english = count_entire - count_hangul
print("한글 : {} , 영어 : {} 전체 : {}" .format(count_hangul, count_english, count_entire))
dt = datetime.datetime.now()
current_date = "{}.{}.{}".format(str(dt.year), str(dt.month), str(dt.day))
current_data = "{} {} {} {}\n".format(current_date, count_entire, count_english, count_hangul)
flag = 0

with open("comment_data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        if current_date in line:
            flag = 1
            break

if flag == 0:
    with open("comment_data.txt", "a") as f:
        f.write(current_data)

date = list()
date.append(current_date)
date.append("2020.2.7")
list_hangul = [count_hangul, 100]
list_english = [count_english, 1400]
list_entire = [count_entire, 1600]

plt.plot(date, list_entire, label='전체')
plt.plot(date, list_english, label="영어댓글")
plt.plot(date, list_hangul, label="한글댓글")


plt.xlabel("날짜")
plt.ylabel("댓글수")
plt.title("BTS (방탄소년단) MAP OF THE SOUL : 7 'Outro : Ego' Comeback Trailer")
plt.legend()

plt.show()

