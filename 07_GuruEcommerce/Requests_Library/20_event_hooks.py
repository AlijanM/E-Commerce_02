# https://www.tutorialspoint.com/requests/requests_event_hooks.htm
# adding events to the URL requested using event hooks, here: a callback function that will get called when the response is available
import requests

# one event hook
def printData(r, *args, **kwargs):
    print(r.url)
    print(r.text)
getdataOneCallback = requests.get('https://jsonplaceholder.typicode.com/users/1', hooks={'response': printData})

# two event hooks
def printRequestedUrl(r, *args, **kwargs):
   print(r.url)
def printData(r, *args, **kwargs):
   print(r.text)
getdataMultipleCallback = requests.get('https://jsonplaceholder.typicode.com/users/1', hooks = {'response': [printRequestedUrl, printData]})

# adding the hook to the Session created
def printData(r, *args, **kwargs):
   print(r.text)
s = requests.Session()
s.hooks['response'].append(printData)
s.get('https://jsonplaceholder.typicode.com/users/1')

# python -s Requests_Library\20_event_hooks.py