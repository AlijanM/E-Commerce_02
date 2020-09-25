from utilities.execution_status import ExecutionStatus
from pages.mobile_items.disabled_fields_page import DisabledFields
import unittest
import pytest

# # Verify user is able to reorder/change placed order
# 1. precondition: User account must have a placed order in status Pending.
# Account "abc11@hotmail.com", "newpass11" has such an order 100012396


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DisabledFieldsTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.df = DisabledFields(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_verifyDisabledFields(self):
        result = self.df.verifyDisabledFields()
        self.es.markFinal("test_1_verifyDisabledFields", result, "Verification of Disabled Fields")


#py.test -s -v tests\mobile_items\test_15_disabled_fields.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html