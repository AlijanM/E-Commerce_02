# https://www.tutorialspoint.com/requests/requests_proxy.htm
'''
- No proxy: clients directly connecting and talking to the server.
- Using proxy, the interaction happens as follows:
1. The client sends a request to the proxy.
2. The proxy sends the request to the server.
3. The server sends back the response to the proxy.
4. The proxy will send a response back to the client.
Using Http-proxy is additional security assigned to manage the data exchange between client and server.
The requests libraries also have provision to handle proxy, by using the proxies param as shown below:
'''

import requests
proxies = {
'http': 'http://localhost:8080'
}
res = requests.get('https://httpbin.org/', proxies=proxies)
print(res.status_code)

# python -s Requests_Library\21_using_proxy.py