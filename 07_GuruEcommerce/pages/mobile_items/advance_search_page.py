import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select

class AdvancedSearch(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _advance_search_link = "//a[contains(text(),'Advanced Search')]"
    _price_from_field = "price"
    _price_to_field = "price_to"
    _search_button = "//button[@class='button']//span//span[contains(text(),'Search')]"
    _xperia_price = "//span[contains(text(),'$100.00')]"
    _galaxy_price = "//span[contains(text(),'$130.00')]"

    ############################
    ### Element Interactions ###
    ############################

    def clickAdvanceSearch(self):
        self.elementClick(locator=self._advance_search_link, locatorType="xpath")

    def enterPriceFromField(self, priceFrom):
        self.sendKeys(priceFrom, locator=self._price_from_field)

    def enterPriceToField(self, priceTo):
        self.sendKeys(priceTo, locator=self._price_to_field)

    def clickSearchButton(self):
        self.elementClick(locator=self._search_button, locatorType="xpath")

    def getXperiaPrice(self):
        XperiaPrice = self.getText(locator=self._xperia_price, locatorType="xpath")
        return XperiaPrice

    def getGalaxyPrice(self):
        galaxyPrice = self.getText(locator=self._galaxy_price, locatorType="xpath")
        return galaxyPrice

    def verifySearchResults(self, priceFrom, priceTo):
        self.clickAdvanceSearch()
        self.enterPriceFromField(priceFrom)
        self.enterPriceToField(priceTo)
        self.clickSearchButton()
        xperiaPrice = self.getXperiaPrice()
        galaxyPrice = self.getGalaxyPrice()

        # if xperiaPrice == "$100.00" and galaxyPrice == "$130.00":
        #     result = True
        # else:
        #     result = False
        #
        # return result

        # return True if (xperiaPrice == "$100.00" and galaxyPrice == "$130.00") else False

        return xperiaPrice == "$100.00" and galaxyPrice == "$130.00"


