from utilities.execution_status import ExecutionStatus
from pages.mobile_items.product_prices_page import ProductPrices
import unittest
import pytest
import requests

class VerifyStatusCodeTest(unittest.TestCase):

    def test_verifyStatusCode(self):

        r = requests.get('https://postman-echo.com/get')

        if r.status_code == 2000:
            print("Test Passed")
        else:
            print("Test Failed")


# python -s Requests_Library\02_response.py