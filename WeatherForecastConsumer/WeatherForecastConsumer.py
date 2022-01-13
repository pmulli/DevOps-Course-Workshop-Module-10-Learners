import requests
import json

def get_token(auth_url, client_id, scope, client_secret, grant_type = 'client_credentials'):
    """
     return: tuple dict with access_token, status_code
        {'access_token': 'tokenid'
        'expires_in': 3600,
        'ext_expires_in': 0,
        'token_type': 'Bearer'}, 200
    """
    # Request access token:
    # https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow#request-an-access-token

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    url =auth_url
    data = { "client_id": client_id,
            "scope": scope,
            "client_secret": client_secret,
            "grant_type": grant_type
        }
    # requests doc http://docs.python-requests.org/en/v0.10.7/user/quickstart/#custom-headers
    r = requests.post(url=url, data=data, headers=headers)

    return r.json(), r.status_code

# Change these vars to test:
auth_url = 'https://login.microsoftonline.com/e5aeb051-16c8-4c3a-b256-598a2d979005/oauth2/v2.0/token'
client_id = 'ae924da3-98f5-4e29-8c17-8a9309bbecfd'
scope = 'api://2dc3c485-5a70-4cf7-92c3-f72ec8998fc7/.default'
client_secret = "GAT7Q~~.9SAjTQCw_Oepy6urer3hyZgh0h7-4"


url = 'http://localhost:5000/WeatherForecast'
get_token = get_token(auth_url, client_id, scope, client_secret)
access_token = get_token[0]['access_token']
header_token = {"Authorization": "Bearer {}".format(access_token)}
rt = requests.get(url=url, headers=header_token)
print(rt.text)