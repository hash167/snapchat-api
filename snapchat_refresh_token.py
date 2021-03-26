import json
from requests_oauthlib import OAuth2Session
import requests

scope = ['snapchat-marketing-api']
authorize_url = 'https://accounts.snapchat.com/login/oauth2/authorize'
access_token_url = 'https://accounts.snapchat.com/login/oauth2/access_token'
protected_url = 'https://adsapi.snapchat.com/v1/me/organizations'

with open('snapchat_credentials.json', 'r') as f:
    snap_credentials = json.load(f)


oauth = OAuth2Session(
    snap_credentials['client_id'],
    redirect_uri=snap_credentials['redirect_url'],
    scope=scope
)

authorization_url, state = oauth.authorization_url(authorize_url)
print('Please go to %s and authorize access.' % authorization_url)


authorization_response = input('Enter the full callback URL: ')

token = oauth.fetch_token(
    access_token_url,
    authorization_response=authorization_response,
    client_secret=snap_credentials['client_secret'],
    scope=scope
)

snap_credentials['access_token'] = oauth.token['access_token']
snap_credentials['refresh_token'] = oauth.token['refresh_token']

print(snap_credentials['refresh_token'])