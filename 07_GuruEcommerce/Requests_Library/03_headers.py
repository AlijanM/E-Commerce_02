# https://www.tutorialspoint.com/requests/requests_http_requests_headers.htm

import requests

# There are three types of headers: request Headers, custom Headers and response Headers

# Request Headers
reqHeaders = requests.get('https://jsonplaceholder.typicode.com/users', stream=True)

# Custom Headers
customHeaders = {'x-user': 'test123'}
custHeaders = requests.get('https://jsonplaceholder.typicode.com/users', headers=customHeaders)

# Response Headers
respHeaders = requests.get('https://jsonplaceholder.typicode.com/users')

print("Request headers: %s \n" % reqHeaders.headers)
print("Custom headers: %s \n" % custHeaders.headers)
print("Response headers: %s \n" % respHeaders.headers)

# print values of some response headers in two methods
print("Value of the response header 'Expect-CT' is: %s \n" % respHeaders.headers["Expect-CT"])
print("Value of the response header 'Content-Type' is: %s \n" % respHeaders.headers.get("Content-Type"))

# python -s Requests_Library\03_headers.py