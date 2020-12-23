# YoutubeApi_test.py code Analyze

This docs explains my python files to understand my functions in files

This docs updates continuously, - SangYun LEE



### First.

Using youtube Api, you should bring your OAuth 2.0 client ID json file

```python
CLIENT_SECRETS_FILE = "your json file"
SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
```

And Create the flow using the client secrets file from the Google API

```python
flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
credentials = flow.run_console()
```

***class* `InstalledAppFlow`(*oauth2session*, *client_type*, *client_config*, *redirect_uri=None*, *code_verifier=None*, *autogenerate_code_verifier=False*)**

Bases: [`google_auth_oauthlib.flow.Flow`](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.Flow)

Authorization flow helper for installed applications.

This [`Flow`](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.Flow) subclass makes it easier to perform the [Installed Application Authorization Flow](https://developers.google.com/api-client-library/python/auth/installed-app). This flow is useful for local development or applications that are installed on a desktop operating system.

This flow has two strategies: The console strategy provided by [`run_console()`](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_console) and the local server strategy provided by [`run_local_server()`](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.run_local_server).



**`run_console`(*authorization_prompt_message='Please visit this URL to authorize this application: {url}'*, *authorization_code_message='Enter the authorization code: '*, ***kwargs*)

Run the flow using the console strategy.

The console strategy instructs the user to open the authorization URL in their browser. Once the authorization is complete the authorization server will give the user a code. The user then must copy & paste this code into the application. The code is then exchanged for a token.

| Parameters:  | **authorization_prompt_message** ([*str*](https://docs.python.org/3.5/library/stdtypes.html#str)) – The message to display to tell the user to navigate to the authorization URL.**authorization_code_message** ([*str*](https://docs.python.org/3.5/library/stdtypes.html#str)) – The message to display when prompting the user for the authorization code.                                                   **kwargs** – Additional keyword arguments passed through to [`authorization_url()`](https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html#google_auth_oauthlib.flow.InstalledAppFlow.authorization_url). |
| :----------- | ------------------------------------------------------------ |
| Returns:     | The OAuth 2.0 credentials for the user.                      |
| Return type: | [google.oauth2.credentials.Credentials](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html#google.oauth2.credentials.Credentials) |



#### Using python os environment variable

```python
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
```

**OAUTHLIB_INSECURE_TRANSPORT**

Normally, OAuthLib will raise an `InsecureTransportError` if you attempt to use OAuth2 over HTTP, rather than HTTPS. Setting this environment variable will prevent this error from being raised. This is mostly useful for local testing, or automated tests. *Never* set this variable in production.



## Comment Results dict

```python
results = f_service.commentThreads().list(**kwargs).execute()
results['items']['snippet']['topLevelComment']['snippet']
```

###### in results, dictionary is made that format.

```python
"snippet": {
    "authorDisplayName": string,
    "authorProfileImageUrl": string,
    "authorChannelUrl": string,
    "authorChannelId": {
      "value": string
    },
    "channelId": string,
    "videoId": string,
    "textDisplay": string,
    "textOriginal": string,
    "parentId": string,
    "canRate": boolean,
    "viewerRating": string,
    "likeCount": unsigned integer,
    "moderationStatus": string,
    "publishedAt": datetime,
    "updatedAt": datetime
  }
```

### snippet. format explanation

| `snippet.authorDisplayName`     | `string` The display name of the user who posted the comment. |
| ------------------------------- | ------------------------------------------------------------ |
| `snippet.authorProfileImageUrl` | `string` The URL for the avatar of the user who posted the comment. |
| `snippet.authorChannelUrl`      | `string` The URL of the comment author's YouTube channel, if available. |
| `snippet.authorChannelId`       | `object` This object encapsulates information about the comment author's YouTube channel, if available. |
| `snippet.authorChannelId.value` | `string` The ID of the comment author's YouTube channel, if available. |
| `snippet.channelId`             | `string` The ID of the YouTube channel associated with the comment.If the comment is a video comment, then this property identifies the video's channel, and the `snippet.videoId` property identifies the video.If the comment is a channel comment, then this property identifies the channel that the comment is about. |
| `snippet.videoId`               | `string` The ID of the video that the comment refers to. This property is only present if the comment was made on a video. |
| `snippet.textDisplay`           | `string` The comment's text. The text can be retrieved in either plain text or HTML. (The `comments.list` and `commentThreads.list` methods both support a `textFormat` parameter, which specifies the desired text format.)  Note that even the plain text may differ from the original comment text. For example, it may replace video links with video titles. |
| `snippet.textOriginal`          | `string` The original, raw text of the comment as it was initially posted or last updated. The original text is only returned if it is accessible to the authenticated user, which is only guaranteed if the user is the comment's author. |
| `snippet.parentId`              | `string` The unique ID of the parent comment. This property is only set if the comment was submitted as a reply to another comment. |
| `snippet.canRate`               | `boolean` This setting indicates whether the current viewer can rate the comment. |
| `snippet.viewerRating`          | `string` The rating the viewer has given to this comment. Note that this property does not currently identify `dislike` ratings, though this behavior is subject to change. In the meantime, the property value is `like` if the viewer has rated the comment positively. The value is `none` in all other cases, including the user having given the comment a negative rating or not having rated the comment.  Valid values for this property are:`like``none` |
| `snippet.likeCount`             | `unsigned integer` The total number of likes (positive ratings) the comment has received. |
| `snippet.moderationStatus`      | `string` The comment's moderation status. This property is only returned if the API request was authorized by the owner of the channel or the video on which the requested comments were made. In addition, note that this property is not set if the API request used the `id` filter parameter.  Valid values for this property are:`heldForReview``likelySpam``published``rejected` |
| `snippet.publishedAt`           | `datetime` The date and time when the comment was orignally published. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format. |
| `snippet.updatedAt`             | `datetime` The date and time when the comment was last updated. The value is specified in [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format. |

