# https://www.tutorialspoint.com/requests/requests_handling_get_requests.htm

import requests

url = 'https://jsonplaceholder.typicode.com/users'
# fetching all users
users = requests.get(url)

# fetching a specific user, here: Delphine
payload = ({'id': 9, 'username': 'Delphine'})
oneUser = requests.get(url, params=payload)

# response (contains alla users) in text
usersT = users.text

# response (contains a specific user, here: Delphine) in text
oneUserT = oneUser.text

print("All users: %s \n" % usersT)
print("A specific user: %s \n" % oneUserT)

# python -s Requests_Library\04_GET_requests.py