# https://www.tutorialspoint.com/requests/requests_handling_post_put_patch_delete_requests.htm

import requests

url = 'https://postman-echo.com/patch'

# pass the form data as key-value pair to Update/Modify entry or resource
modifiedUser = requests.patch(url, data="testing PATCH method")

# response (contains the Updated/Modified user) in text
modifiedUserT = modifiedUser.text

print("Modified user: %s \n" % modifiedUserT)


# python -s Requests_Library\07_PATCH_requests.py