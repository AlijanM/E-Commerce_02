# https://www.tutorialspoint.com/requests/requests_handling_response_for_http_requests.htm

import requests

# 'r' has the response object
r = requests.get('https://jsonplaceholder.typicode.com/users')

# response in text
rt = r.text

# response in 'content'
rc = r.content

# response in json
# rs = r.json()

print("Response object: ", r)
print("Response body in text: ", rt)
print("Response body in 'content': ", rc)
# print("Response body in json: ", rs)


# python -s Requests_Library\02_response.py