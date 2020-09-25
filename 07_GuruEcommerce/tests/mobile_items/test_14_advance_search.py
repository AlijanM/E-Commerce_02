from utilities.execution_status import ExecutionStatus
from pages.mobile_items.advance_search_page import AdvancedSearch
import unittest
import pytest

# Verify items in Mobile List page can be sorted by 'Name'

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AdvanceSearch(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.advSearch = AdvancedSearch(self.driver)
        self.es = ExecutionStatus(self.driver)

    #@pytest.mark.run(order=1)
    def test_1_serachedPrices(self):
        result1 = self.advSearch.verifySearchResults("0", "150")
        self.es.markFinal("test_1_serachedPrices", result1, "Verification of test_1_serached Prices")


    # #@pytest.mark.run(order=2)
    # def test_2_mobilePage(self):
    #     result1 = self.sbn.verifyMobilePageTitle("Mobile")
    #     self.es.mark(result1, "Verification of Page Title")
    #
    #     result2 = self.sbn.verifySortByName()
    #     self.es.markFinal("test_mobilePage", result2, "Verification of Product Sorting")

#py.test -s -v tests\mobile_items\test_14_advance_search.py --browser chrome --html=C:\Users\semc0\Desktop\TestReport\tp.html
