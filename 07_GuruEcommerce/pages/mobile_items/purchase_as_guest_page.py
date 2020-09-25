import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select

class PurchaseAsGuest(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _mobile_menu = "//a[contains(text(),'Mobile')]"
    _iphone_button = "//ul[@class='products-grid products-grid--max-4-col first last odd']/li[2]//span[contains(text(),'Add to Cart')]"
    _update_shopping_card_link = "//span[contains(text(),'Update Shopping Cart')]"
    _checkout_button = "//ul[@class='checkout-types top']//span[contains(text(),'Proceed to Checkout')]"
    _continue_button = "//button[@id='onepage-guest-register-button']//span[contains(text(),'Continue')]"

    # shipping information
    _first_name_field = "billing:firstname"  # id
    _last_nae_field = "billing:lastname"  # id
    _email_field = "billing:email" # id
    _address_field = "billing:street1"  # id
    _city_field = "billing:city"  # id
    _state_province_field = "billing:region_id"  # id
    _zip_field = "billing:postcode"  # id
    _telephone_field = "billing:telephone"  # id
    _continue_button1 = "//div[@id='billing-buttons-container']//span[contains(text(),'Continue')]"
    _continue_button2 = "//div[@id='shipping-method-buttons-container']//button[@class='button']//span//span[contains(text(),'Continue')]"

    _flat_rate = "//span[@class='price'][contains(text(),'$5.00')]"  # enhetspris //span[contains(text(),'$10.00')]
    _money_order_radioBtn = "//label[@for='p_method_checkmo'][contains(text(),'Check / Money order')]"
    _continue_button3 = "//div[@id='payment-buttons-container']//button[@class='button']//span//span[contains(text(),'Continue')]"  # "//*[@id='payment-buttons-container']/button"

    _sub_total = "//tr[@class='first']//span[@class='price'][contains(text(),'$615.00')]"
    _grand_total = "//span[contains(text(),'$620.00')]"

    _place_order_button = "//span[contains(text(),'Place Order')]"  # //div[@id='checkout-review-submit']//span[contains(text(),'Place Order')]

    _order_confirmation = "//div[@class='page-title']/h1[contains(text(),'Your order has been received.')]"


    ############################
    ### Element Interactions ###
    ############################

    def clickMobileMenu(self):
        self.elementClick(locator=self._mobile_menu, locatorType="xpath")

    def clickIphoneButton(self):
        self.elementClick(locator=self._iphone_button, locatorType="xpath")

    def clickUpdateLink(self):
        self.elementClick(locator=self._update_shopping_card_link, locatorType="xpath")

    def clickCheckoutButton(self):
        self.elementClick(locator=self._checkout_button, locatorType="xpath")

    def clickContinueButton(self):
        self.elementClick(locator=self._continue_button, locatorType="xpath")

    def enterFirstName(self, fname):
       self.sendKeys(fname, locator=self._first_name_field)

    def enterLastName(self, lname):
       self.sendKeys(lname, locator=self._last_nae_field)

    def enterEmail(self, email):
       self.sendKeys(email, locator=self._email_field)

    def enterAddress(self, address):
        self.sendKeys(address, locator=self._address_field)

    def enterCity(self, city):
        self.sendKeys(city, locator=self._city_field)

    def selectState(self):
        state = self.getElement(locator=self._state_province_field)
        sel = Select(state)
        sel.select_by_value("43")

    def enterZip(self, zip):
        self.sendKeys(zip, locator=self._zip_field)

    def enterTelephone(self, number):
        self.sendKeys(number, locator=self._telephone_field)

    def clickContinueBtn1(self):
        self.elementClick(locator=self._continue_button1, locatorType="xpath")

    def clickContinueBtn2(self):
        self.elementClick(locator=self._continue_button2, locatorType="xpath")

    def isFlatRateDisplayed(self):
        # txt = self.getText(locator=self._flat_rate, locatorType="xpath")
        # return txt
        display = self.isElementDisplayed(locator=self._flat_rate, locatorType="xpath")
        return display

    def clickMoneyOrderRadioBtn(self):
        self.elementClick(locator=self._money_order_radioBtn, locatorType="xpath")

    def clickContinueBtn3(self):
        self.elementClick(locator=self._continue_button3, locatorType="xpath")

    def clickPlaceOrderBtn(self):
        self.elementClick(locator=self._place_order_button, locatorType="xpath")

    def shoppingCard(self):
        self.clickMobileMenu()
        self.clickIphoneButton()
        self.clickUpdateLink()
        self.clickCheckoutButton()
        self.clickContinueButton()

    def billingInfo(self, fname, lname, email, address, city, zip, number):
        self.enterFirstName(fname)
        self.enterLastName(lname)
        self.enterEmail(email)
        self.enterAddress(address)
        self.enterCity(city)
        self.selectState()
        self.enterZip(zip)
        self.enterTelephone(number)
        self.clickContinueBtn1()
        self.clickContinueBtn2()
        self.clickMoneyOrderRadioBtn()
        self.clickContinueBtn3()
        self.clickPlaceOrderBtn()


    def verifyTitle(self):
        self.shoppingCard()
        self.billingInfo("fname", "lname", "abc@email.com", "ABC", "New York", "542896", "12345678")
        # self.enterShippingInfo("ABC", "New York", "542896", "12345678")

        orderConf = self.getText(locator=self._order_confirmation, locatorType="xpath")

        return orderConf == 'YOUR ORDER HAS BEEN RECEIVED.'