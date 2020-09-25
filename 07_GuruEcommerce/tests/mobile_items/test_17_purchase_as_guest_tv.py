from utilities.execution_status import ExecutionStatus
from pages.mobile_items.purchase_as_guest_tv_page import PurchaseAsGuestTv
import unittest
import pytest

# Verify Sort is working correctly


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PurchaseAsGuestTvTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ptv = PurchaseAsGuestTv(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_verifyOrderPurchase(self):
        result = self.ptv.verifyTitle()
        self.es.markFinal("test_verifyPurchase", result, "Verification of Shopping")


#py.test -s -v tests\mobile_items\test_17_purchase_as_guest_tv.py --browser chrome --html=C:\Users\AlijanMo\Desktop\TestReport\Guru99\tp.html