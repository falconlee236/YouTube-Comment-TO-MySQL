import pickle
import os
import csv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

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
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comment2 = item['snippet']['topLevelComment']['snippet']['publishedAt']
            comment3 = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comments['textDisplay'] = comment
            comments['publishedAt'] = comment2
            comments['authorDisplayName'] = comment3
            if "replies" in item:
                for i in range(len(item["replies"]["comments"])):
                    rep_comments = {}
                    rep_comment = item["replies"]["comments"][i]['snippet']['textDisplay']
                    rep_comment2 = item["replies"]["comments"][i]['snippet']['publishedAt']
                    rep_comment3 = item["replies"]["comments"][i]['snippet']['authorDisplayName']
                    rep_comments['textDisplay'] = rep_comment
                    rep_comments['publishedAt'] = rep_comment2
                    rep_comments['authorDisplayName'] = rep_comment3
                    comments["reply_comment" + str(i + 1)] = rep_comments

            comment_list.append(comments)

        # Check if another page exists
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = service.commentThreads().list(**kwargs).execute()
        else:
            break

    return comment_list


def write_to_csv(comments):
    with open('comments.csv', 'w') as comments_file:
        comments_writer = csv.writer(comments_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        comments_writer.writerow(['Video ID', 'Title', 'Comment'])
        for row in comments:
            comments_writer.writerow(row.values())


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    video_id = input('Enter a video_id: ')
    total = get_video_comments(service, part=['snippet', 'replies'],
                               videoId=video_id, textFormat='plainText', maxResults=100)
    write_to_csv(total)
    for x in total:
        print(x)
    print(len(total))


# 여백의 미
#https://youtu.be/TggWNRMPboo

#BTS DYNAMAITE 10,000,000개 댓글 있음
#https://youtu.be/gdZLi9oWNZg
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