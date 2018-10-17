from pages.home.login_page import LoginPage
from utilities.status import Status
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lg = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def tests_validLogin(self):
        self.lg.login('qatesteratx@gmail.com', 'test1234')
        result1 = self.lg.verifyTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lg.verifySuccessfulLogin()
        self.ts.markFinal("tests_validLogin", result2, "Login Verification")

    # @pytest.mark.run(order=1)
    # def tests_invalidLogin(self):
    #     self.lg.login()
    #     result = self.lg.verifyFailedLogin()
    #     assert result == True
