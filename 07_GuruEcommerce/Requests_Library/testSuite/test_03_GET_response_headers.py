from utilities.execution_status import ExecutionStatus
from pages.mobile_items.product_prices_page import ProductPrices
import unittest
import pytest
import requests

class VerifyResponseHeadersTest(unittest.TestCase):

    def test_verifyResponseHeaders(self):
        #the required first parameter of the 'get' method is the 'url':
        r = requests.get('https://postman-echo.com/get')

        #print the response text (the content of the requested file):
        print("Response headers: ", r.headers)

        hd = r.headers.get('Date')
        hct = r.headers['Content-Type']

        print("Headers date: ", hd)
        print("Headers content type: ", hct)


        if hct == "application/json; charset=utf-8":
            print("Test Passed")
        else:
            print("Test Failed")

# python -s Requests_Library\03_headers.py