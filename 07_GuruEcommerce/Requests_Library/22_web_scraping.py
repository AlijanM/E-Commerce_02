# https://www.tutorialspoint.com/requests/requests_web_scraping_using_requests.htm
'''
1. Install Beautiful Soup: pip install beautifulsoup4
2. We will try to scrap (= extracting underlying HTML code and, with it, data stored in a database) the data from the
site of Tutorialspoint which is available at https://www.tutorialspoint.com/tutorialslibrary.htm using the following:
- Requests Library
- Beautiful soup library from python
'''

import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.tutorialspoint.com/tutorialslibrary.htm')
print("The status code is:", res.status_code)
print("\n")
soup_data = BeautifulSoup(res.text, 'html.parser')
print("The title is:", soup_data.title.text)
print("\n")
print(soup_data.find_all('h4'))

# python -s Requests_Library\22_web_scraping.py