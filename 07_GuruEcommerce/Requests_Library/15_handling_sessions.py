# https://www.tutorialspoint.com/requests/requests_handling_sessions.htm
import requests

# sessions is used to maintain the data (e.g. cookies) between requests,  pass headers data...

# using sessions to maintain data (here: cookies) between requests
url = 'https://httpbin.org/cookies'
reqC = requests.Session()
cookies = dict(test='test123')
getData = reqC.get(url, cookies=cookies)
print(getData.text)

# using session to pass headers data
reqH = requests.Session()
reqH.headers.update({'x-user1': 'ABC'})
headers = {'x-user2': 'XYZ'}
getdata = reqH.get('https://httpbin.org/headers', headers=headers)
print(getdata.headers)

# python -s Requests_Library\15_handling_sessions.py