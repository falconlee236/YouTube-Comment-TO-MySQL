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

