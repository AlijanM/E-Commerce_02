# https://www.tutorialspoint.com/requests/requests_handling_post_put_patch_delete_requests.htm

import requests

url = 'https://postman-echo.com/put'

# pass the form data as key-value pair to Update/Replace entry or resource
myParams = {'name': 'ABC', 'email': 'wxyz@gmail.com'}
replacedUser = requests.put(url, data=myParams)

# response (contains the Updated/Replaced user) in text
replacedUserT = replacedUser.text

print("Replaced user: %s \n" % replacedUserT)


# python -s Requests_Library\06_PUT_requests.py