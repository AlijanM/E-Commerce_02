# https://www.tutorialspoint.com/requests/requests_authentication.htm

# If server asks client for authentication information, e.g. username and password, for providing response/data:
# 1. client sends authentication information in the request headers when requesting a URL
# 2. server validate the information, i.e. required data will delivered if the authentication is valid

import requests
from requests.auth import HTTPBasicAuth

# Basic authentication
url = "https://httpbin.org/basic-auth/admin/admin123"
response_data = requests.get(url, auth=HTTPBasicAuth('admin', 'admin123'))
print(response_data.text)

# python -s Requests_Library\17_authentication_basic.py