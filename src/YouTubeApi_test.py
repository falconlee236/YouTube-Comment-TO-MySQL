import pickle
import csv
import os

import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# your OAuth 2.0 client ID json file
CLIENT_SECRETS_FILE = "client_secret_lsy.json"
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
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
            # Create the flow using the client secrets file from the Google API
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_console()

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)



def get_video_comments(service, **kwargs):
    comments = []
    results = service.commentThreads().list(**kwargs).execute()

    while results:
      for item in results['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comment2 = item['snippet']['topLevelComment']['snippet']['publishedAt']
        comment3 = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        print(comment)
        print(comment2)
        print(comment3)
        print('==============================')
        comments.append(comment)

      # Check if another page exists
      if 'nextPageToken' in results:
        kwargs['pageToken'] = results['nextPageToken']
        results = service.commentThreads().list(**kwargs).execute()
      else:
        break

    return comments


if __name__ == '__main__':
    # When running locally, disable OAuthlib's HTTPs verification. When
    # running in production *do not* leave this option enabled.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    service = get_authenticated_service()
    video_id = input('Enter a video_id: ')
    get_video_comments(service, part='snippet', videoId=video_id, textFormat='plainText')

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