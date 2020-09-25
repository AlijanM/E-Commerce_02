# https://www.tutorialspoint.com/requests/requests_handling_redirection.htm
import requests

url = 'http://google.com/'
getData = requests.get(url)

# The redirection:  status code is 301 and will be saved in the history
print("########## Redirection Allowed ##########")
print(getData.status_code)
print("History - Redirection allowed: %s \n" % getData.history)

# Redirection can be stopped. It can be done on GET, POST, OPTIONS, PUT, DELETE, PATCH methods
getDataNoRedir = requests.get(url, allow_redirects=False)
print("########## Redirection Not Allowed ##########")
print("Status code - No Redirection: %s" % getDataNoRedir.status_code)
print("History - No Redirection: %s" % getDataNoRedir.history)
print("Response body - No Redirection:\n%s" % getDataNoRedir.text)

# python -s Requests_Library\13_handling_redirection.py