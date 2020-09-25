# https://www.tutorialspoint.com/requests/requests_handling_history.htm
import requests

url = 'http://google.com/'
getData = requests.get(url)

# get the history of a given URL by using response.history.
# If the given URL has any redirects, the same will be stored in history.
print("########## Redirection Allowed ##########")
print(getData.status_code)
print("History - Redirection allowed: %s \n" % getData.history)

# python -s Requests_Library\14_handling_history.py