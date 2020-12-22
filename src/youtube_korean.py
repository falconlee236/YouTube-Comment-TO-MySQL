# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from bs4 import BeautifulSoup
from IPython.display import display
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import datetime
import time
import re


def isHangul(text):
    hancount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', text))
    return hancount > 0


def webdriver_excute(url):
    # Webdriver Execute
    driver = wd.Chrome(executable_path="chromedriver.exe")
    driver.get(url)

    # execute_script() running js file
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
    return html_source


def make_plot(cur_date, entire, english, korean):
    # noinspection PyUnresolvedReferences
    matplotlib.font_manager._rebuild()
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2)
    ax3 = fig.add_subplot(1, 3, 3)

    ax1.plot(cur_date, entire, label='Total')
    ax2.plot(cur_date, english, label="English Comment")
    ax3.plot(cur_date, korean, label="Korean Comment")

    plt.xlabel("Date")
    plt.ylabel("Comments")
    plt.title("BTS MAP OF THE SOUL : 7 'Outro : Ego' Comeback Trailer")

    ax1.legend()
    ax2.legend()
    ax3.legend()

    plt.show()


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=LmApDbvNCXg"
    soup = BeautifulSoup(webdriver_excute(url), 'lxml')
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
    # 화면 출력 코드
    display(youtube_pd)
    count_entire = youtube_pd.shape[0]

    count_hangul = 0
    for x in youtube_pd["Comment"]:
        if isHangul(x) is True:
            count_hangul += 1

    count_english = count_entire - count_hangul
    print("한글 : {} , 영어 : {} 전체 : {}".format(count_hangul, count_english, count_entire))
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
    list_hangul = list()
    list_english = list()
    list_entire = list()
    data = list()
    count = 0
    with open("comment_data.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            count += 1
            data = line.split()
            date.append(data[0])
            list_entire.append(int(data[1]))
            list_english.append(int(data[2]))
            list_hangul.append(int(data[3]))

    make_plot(date, list_entire, list_english, list_hangul)







