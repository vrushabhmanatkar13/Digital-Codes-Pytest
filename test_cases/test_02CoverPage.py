from urllib import request

import allure
import pytest
from test_cases.test_base import TestBase
from utiilites import read_excle
from utiilites.BaseClass import BaseClass
from utiilites.Logger import get_logger


@allure.feature("Cover Page")
class Test_CoverPage(TestBase):

    @allure.title("Class Setup")
    def test_classSetup(self):
        user_data=read_excle.get_data_for_smoke("login","Verify Login with valid username and password")
        self.headerpage.click_Signin()
        self.loginpage.login(user_data[0], user_data[1])


    @allure.title("Test Title Cover")
    @allure.tag("Cover Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that user able to navigate cover page")
    @pytest.mark.parametrize(["OptionL1", "OptionL2", "OptionL3"], read_excle.get_data("Cover Page", "Verify Navigate to Cover Page"))
    def test_verify_Title_Cover(self, request, OptionL1, OptionL2, OptionL3):
        test_logger = get_logger(request.node.name)
        self.headerpage.click_menu()
        self.headerpage.click_menu_option(OptionL1)
        self.headerpage.click_menu_option(OptionL2)
        self.headerpage.click_menu_sub_option(OptionL3)
        title = self.baseclass.wait_title_is(OptionL3+" Building Codes - ICC Digital Codes")
        heading = self.coverpage.get_page_heading()
        BaseClass.assert_True(title, test_logger)
        BaseClass.assert_equals(OptionL3, heading, test_logger)
