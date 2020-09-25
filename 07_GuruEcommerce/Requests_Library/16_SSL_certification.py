# https://www.tutorialspoint.com/requests/requests_ssl_certification.htm

import requests
url = "https://jsonplaceholder.typicode.com/users/1"
# SSL verification enabled --> no ssl-warning message
getdataSSL = requests.get(url)
print("########## SSL verification enabled ##########")
print(getdataSSL.text)

# SSL verification disabled --> ssl-warning message
getdata = requests.get(url, verify=False)
print("########## SSL verification disabled ##########")
print(getdata.text)

# python -s Requests_Library\16_SSL_certification.py