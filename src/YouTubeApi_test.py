import pickle
import os
import csv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pandas
import pymysql
import json
import re
from emoji import UNICODE_EMOJI


def is_emoji(s):
    return s in UNICODE_EMOJI


# your OAuth 2.0 client ID json file
CLIENT_SECRETS_FILE = "client_secret_lsy.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


def get_authenticated_service():
    credentials = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)
    #  Check if the credentials are invalid or do not exist
    if not credentials or not credentials.valid:
        # Check if the credentials have expired
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_console()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)


def get_video_comments(f_service, **kwargs):
    comment_list = []
    results = f_service.commentThreads().list(**kwargs).execute()
    count = 1
    while results:
        for item in results['items']:
            print(count)
            count += 1
            comments = {}
            comment = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment2 = item['snippet']['topLevelComment']['snippet']['publishedAt']
            comment3 = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments['authorDisplayName'] = comment
            comments['publishedAt'] = comment2
            comments['textDisplay'] = comment3
            if "replies" in item:
                for i in range(len(item["replies"]["comments"])):
                    rep_comments = {}
                    rep_comment = item["replies"]["comments"][i]['snippet']['authorDisplayName']
                    rep_comment2 = item["replies"]["comments"][i]['snippet']['publishedAt']
                    rep_comment3 = item["replies"]["comments"][i]['snippet']['textDisplay']
                    rep_comments['authorDisplayName'] = rep_comment
                    rep_comments['publishedAt'] = rep_comment2
                    rep_comments['textDisplay'] = rep_comment3
                    comments["reply_comment" + str(i + 1)] = rep_comments

            comment_list.append(comments)

        # Check if another page exists
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = f_service.commentThreads().list(**kwargs).execute()
        else:
            break

    return comment_list


def write_to_csv(comments):
    with open('comments.csv', 'w') as comments_file:
        comments_writer = csv.writer(comments_file, newline='', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comments_writer.writerow(['Video ID', 'Date', 'Comment'])
        for row in comments:
            comments_writer.writerow(row.values())


def mysql_connect(data):
    with open('MySQL_Auth.json') as auth_file:
        mysql_auth = json.load(auth_file)

        test_db = pymysql.connect(
            user=mysql_auth["user"],
            passwd=mysql_auth["passwd"],
            host=mysql_auth["host"],
            db=mysql_auth["db"],
            charset=mysql_auth["charset"]
        )

        cursor = test_db.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select count(*) as num from causw.youtube_comment;")
        if cursor.fetchall()[0]['num'] == 0:
            sql = 'insert into causw.youtube_comment values (%s, %s, %s, %s);'
            cursor.executemany(sql, data)
            test_db.commit()
        cursor.execute("select * from causw.youtube_comment;")
        result = cursor.fetchall()
        print(pandas.DataFrame(result))


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    video_id = input('Enter a video_id: ')
    total = get_video_comments(service, part=['snippet', 'replies'],
                               videoId=video_id, textFormat='plainText', maxResults=100)
    #"Incorrect string value: '\\xF0\\x9F\\x99\\x87' for column 'comment' at row 89")
    total_tolist = []
    for x in total:
        sublist = [x['authorDisplayName'], x['publishedAt'], x['textDisplay']]
        if len(x) > 3:
            key_count = 1
            reply_str = ""
            for key in x.keys():
                if key_count > 3:
                    reply_list = x[key].values()
                    reply_str += ('-'.join(reply_list) + "|")
                key_count += 1
            sublist.append(reply_str)
        else:
            sublist.append(" ")
        total_tolist.append(sublist)
        for k in re.findall(r'[^\w\s,]', sublist[2]):
            if is_emoji(k) is True:
                sublist[2] = sublist[2].replace(k, "")

        for b in re.findall(r'[^\w\s,]', sublist[3]):
            if is_emoji(b) is True:
                sublist[3] = sublist[3].replace(b, "")

    mysql_connect(total_tolist)

    #write_to_csv(total)
    '''
    for x in total:
        print(x)
    print(len(total))
    '''
    #pd = pandas.read_csv("comments.csv", encoding='cp949', error_bad_lines=False)


    '''
    sql = 'insert into causw.youtube_comment values (%s, %s, %s);'
    total_list = []
    for x in range(pd.shape[0]):
        total_list.append(pd.iloc[x].tolist())
    print(total_list)
    cursor.executemany(sql, total_list)
    test_db.commit()
    '''




# 여백의 미
#https://youtu.be/TggWNRMPboo

#BTS DYNAMAITE 10,000,000개 댓글 있음
#https://youtu.be/gdZLi9oWNZg

#침착맨 삼국지 1500개 댓글
#https://youtu.be/hnanNlDbsE4
'''
from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "mykey"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(
    q="김도랜드",
    order="date",
    part="snippet",
    maxResults=50#max is 50
).execute()

count = 0
for i in search_response['items']:
    print(i['snippet']['title'])
    print("##################################")
'''