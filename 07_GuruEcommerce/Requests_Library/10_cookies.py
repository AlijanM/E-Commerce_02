# https://www.tutorialspoint.com/requests/requests_working_with_cookies.htm

import requests

url = 'https://jsonplaceholder.typicode.com/users'
# fetching all users
users = requests.get(url)

# hitting the url in browser, Dev Tools/Request Headers/cookie: __cfduid=dec2ddc7b7500bf7963228bff74ae9bac1598515679
# where '__cfduid' is the name of the cookie. The cookie can be read as shown below:

print("Cookie in request headers: %s \n" % users.cookies["__cfduid"])

# cookies can also be sent when making request:
myCookies = dict(name='test', id='123')
getdata = requests.get('https://httpbin.org/cookies', cookies=myCookies)
print("Sent cookie is: %s" % getdata.text)

# python -s Requests_Library\10_cookies.py