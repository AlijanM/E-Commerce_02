import requests

r = requests.get('https://jsonplaceholder.typicode.com/users')
sc = r.status_code
print("The status code is: %s" % sc)

# python -s Requests_Library\01_status_code.py