# https://www.tutorialspoint.com/requests/requests_authentication.htm

# If server asks client for authentication information, e.g. username and password, for providing response/data:
# 1. client sends authentication information in the request headers when requesting a URL
# 2. server validate the information, i.e. required data will delivered if the authentication is valid

# OAuth2 authentication. You have to install OAuth2: 'pip install requests_oauth2'
import requests
from requests_oauth2.services import GoogleClient

google_auth = GoogleClient(client_id="xxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com",
   redirect_uri="http://localhost/auth/success.html")
a = google_auth.authorize_url(scope=["profile", "email"], response_type="code")
res = requests.get(a)
print(res.url)

# python -s Requests_Library\19_authentication_OAuth2.py