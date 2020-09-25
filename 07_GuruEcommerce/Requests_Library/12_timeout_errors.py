# https://www.tutorialspoint.com/requests/requests_handling_timeouts.htm
import requests

url = 'https://jsonplaceholder.typicode.com/users'
# when using a third-party URL and waiting for a response
# t =0.001 will give timeout error, but not t =0.1
t = 0.001
# t= 0.1
getData = requests.get(url, timeout=t)
print("Timeout error is: %s \n" % getData.text)


# python -s Requests_Library\12_timeout_errors.py