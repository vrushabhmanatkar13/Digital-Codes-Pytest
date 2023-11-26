import allure
import pytest
from test_cases import test_base

from test_cases.test_base import TestBase
from utiilites import read_excle
from utiilites.BaseClass import BaseClass
from utiilites.Logger import get_logger


@allure.feature("Login Page")
class Test_LoginPage(TestBase):

    @allure.title("Test Login")
    @allure.tag("Login Page")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("Verify that user able to login by enter username, password and click on login")
    @pytest.mark.parametrize(["email", "password", "name", "subscription"],
                             read_excle.get_data("login", "Verify Login with valid username and password"))
    def test_login(self, request, email, password, name, subscription):
        test_logger = get_logger(request.node.name)
        self.headerpage.click_Signin()
        subscription_type = self.loginpage.login(email, password)
        info = self.headerpage.get_name_email()
        title = self.baseclass.wait_title_is("My Library")
        BaseClass.assert_True(title, test_logger)
        BaseClass.assert_equals(subscription, subscription_type, test_logger)
        BaseClass.assert_equals(name, info.get("name"), test_logger)
        BaseClass.assert_equals(email, info.get("email"), test_logger)
