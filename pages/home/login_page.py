from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _signin_link = '.nav> div > div > nav > div > a'
    _email_field = 'email'
    _pwd_field = 'passwd'
    _login_button = 'SubmitLogin'
    _user_id = "//span[contains(text(),'Test Tester')]"

    # Created the action methods that are performed on the elements
    def clickSigninLink(self):
        self.elementClick(self._signin_link, locatorType="css")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._pwd_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    # Wraps all the actions
    def login(self, email="", password=""):
        self.clickSigninLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    # Method to verify login
    def verifySuccessfulLogin(self):
        result = self.isElementPresent(self._user_id, locatorType="xpath")
        return result

    def verifyFailedLogin(self):
        result = self.isElementPresent("//p[contains(text(),'There is 1 error')]", locatorType="xpath")
        if result is True:
            return True
        else:
            return False

    def verifyTitle(self):
        if "My account - My Store" in self.getTitle():
            return True
        else:
            return False
