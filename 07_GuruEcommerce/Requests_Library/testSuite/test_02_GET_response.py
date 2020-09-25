from utilities.execution_status import ExecutionStatus
from pages.mobile_items.product_prices_page import ProductPrices
import unittest
import pytest
import requests

class VerifyResponseTest(unittest.TestCase):

    def test_verifyResponse(self):
        #the required first parameter of the 'get' method is the 'url':
        r = requests.get('https://postman-echo.com/get')

        rt = r.text  # content of response in text
        rs = r.json()  # content of response in json

        print("Response status: ", r)
        print("Response body in text format: ", rt)
        print("Response body in json format: ", rs)

        print("Response headers: ", r.headers)
        print("Response URL: ", r.url)

        if r.url == "https://postman-echo.com/gett":
            print("Test Passed")
        else:
            print("Test Failed")

# python -s Requests_Library\02_response.py