import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.support.ui import Select
import time

# Export all Orders in csv file and display these information in console and
# you are able to send this file to another email id as attachment


class DisabledFields(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################

    _user_name_field = "username"  # id
    _password_field = "login"  # id
    _login_button = "//input[@class='form-button']"  # xpath

    _popup_close_link = "//div[@id='message-popup-window']//a[@title='close']"

    _customers_link = "//a[@class='active']//span[contains(text(),'Customers')]"
    _manage_customers_link = "//span[contains(text(),'Manage Customers')]"

    _customer_id_link = "//td[contains(text(),'42085')]"
    _account_information_link = "//span[contains(text(),'Account Information')]"

    _associated_to_website_field = "_accountwebsite_id"
    _created_from_field = "_accountcreated_in"



    ############################
    ### Element Interactions ###
    ############################

    def enterUserName(self, email):
        self.sendKeys(email, locator=self._user_name_field)

    def enterPaasword(self, password):
        self.sendKeys(password, locator=self._password_field)

    def clickLoginButton(self):
        self.elementClick(locator=self._login_button, locatorType="xpath")

    def clickClosePopupWindow(self):
        self.elementClick(locator=self._popup_close_link, locatorType="xpath")

    def clickCustomersLink(self):
        self.elementClick(locator=self._customers_link, locatorType="xpath")

    def clickManageCustomersLink(self):
        self.elementClick(locator=self._manage_customers_link, locatorType="xpath")

    def clickCustomerIdLink(self):
        self.elementClick(locator=self._customer_id_link, locatorType="xpath")

    def clickAccountInfoLink(self):
        self.elementClick(locator=self._account_information_link, locatorType="xpath")

    def login(self, userName, password):
        self.enterUserName(userName)
        self.enterPaasword(password)
        self.clickLoginButton()


    def navigateToCustoemrInfopage(self, userName, password):
        self.login(userName, password)
        self.clickClosePopupWindow()
        self.clickCustomersLink()
        self.clickManageCustomersLink()
        self.clickCustomerIdLink()
        self.clickAccountInfoLink()

    def verifyDisabledFields(self):
        self.navigateToCustoemrInfopage("user01", "guru99com")
        result1 = self.isEnabled(locator=self._associated_to_website_field)
        result2 = self.isEnabled(locator=self._created_from_field)

        return False if result1 and result2 else True





