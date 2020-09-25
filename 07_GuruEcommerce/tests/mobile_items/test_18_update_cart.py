from utilities.execution_status import ExecutionStatus
from pages.mobile_items.update_cart_page import UpdateCartIphone
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class UpdateShoppingCartIphoneTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.UCI = UpdateCartIphone(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_2_verifySuccessfulPurchase(self):
        result = self.UCI.verifySuccessfullOrder()
        self.es.markFinal("test_2_verifySuccessfulPurchase", result, "Verification of Shopping")

    def test_1_verifyQuantity(self):
        result = self.UCI.verifyUpdatedQuantity()
        self.es.markFinal("test_1_verifyQuantity", result, "Verification of Quantity Update")


#py.test -s -v tests\mobile_items\test_18_update_cart.py --browser chrome --html=C:\Users\AlijanMo\Desktop\TestReport\Guru99\tp.html