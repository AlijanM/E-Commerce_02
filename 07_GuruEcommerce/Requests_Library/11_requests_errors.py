# https://www.tutorialspoint.com/requests/requests_working_with_errors.htm
# Error Exception: ConnectionError, Response.raise_for_status(), HTTPError, Timeout  and TooManyRedirects
# Example below is a timeout  error
import requests

url = 'https://jsonplaceholder.typicode.com/users'

# Timeout error while fetching all users within 0.001 s
getData = requests.get(url, timeout=0.001)

print("Timeout error is: %s \n" % getData.text)


# python -s Requests_Library\11_requests_errors.py