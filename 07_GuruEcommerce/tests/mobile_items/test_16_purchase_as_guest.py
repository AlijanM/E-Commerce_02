from utilities.execution_status import ExecutionStatus
from pages.mobile_items.purchase_as_guest_page import PurchaseAsGuest
import unittest
import pytest

# Verify Sort is working correctly


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PurchaseAsGuestTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.pag = PurchaseAsGuest(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_verifyOrderPurchase(self):
        result = self.pag.verifyTitle()
        self.es.markFinal("test_verifyPurchase", result, "Verification of Shopping")


#py.test -s -v tests\mobile_items\test_16_purchase_as_guest.py --browser chrome --html=C:\Users\AlijanMo\Desktop\TestReport\Guru99\tp1.html