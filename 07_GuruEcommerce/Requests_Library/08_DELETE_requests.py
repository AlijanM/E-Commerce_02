# https://www.tutorialspoint.com/requests/requests_handling_post_put_patch_delete_requests.htm

import requests

url = 'https://postman-echo.com/delete'

# pass the form data as key-value pair to delete entry or resource
deletedUser = requests.delete(url, data="testing DELETE method")

# response (contains the deleted user) in text
deletedUserT = deletedUser.text

print("Deleted user: %s \n" % deletedUserT)


# python -s Requests_Library\08_DELETE_requests.py