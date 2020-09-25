# https://www.tutorialspoint.com/requests/requests_handling_post_put_patch_delete_requests.htm

import requests

url = 'https://postman-echo.com/post'

# pass the form data as key-value pair to create entry or resource
myParams = {'name': 'ABC', 'email': 'xyz@gmail.com'}
newUser = requests.post(url, data=myParams)

# response (contains the new user) in text
newUserT = newUser.text

print("New user: %s \n" % newUserT)


# python -s Requests_Library\05_POST_requests.py