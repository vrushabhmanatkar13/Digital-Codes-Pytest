from re import S
import time

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from page_object.CoverPageObject import CoverPageObject
from page_object.HeaderPageObject import HeaderPageObject
from page_object.LoginPageObject import LoginPageObject
from page_object.My_Notes_Bookmark_Page import My_Notes_Bookmark_Page
from page_object.TOCPageObject import TOCPageObject
from page_object.TitleContentPageObject import TitleContentPageObject
from page_object.TitleLandingPageObject import TitleLandingPageObject
from test_cases.conftest import *
from utiilites.BaseClass import BaseClass


@pytest.mark.usefixtures("Setup_TearDown")
class TestBase:
    driver: WebDriver
    type_test: str

    @pytest.fixture(autouse=True)
    def class_Object(self, get_Environment):
        self.driver.get(get_Environment)  # to reload url before every test
        self.baseclass = BaseClass(self.driver)
        self.headerpage = HeaderPageObject(self.driver, self.baseclass)
        self.loginpage = LoginPageObject(self.driver, self.baseclass)
        self.coverpage = CoverPageObject(self.driver, self.baseclass)
        self.titlelandingpage = TitleLandingPageObject(self.driver, self.baseclass)
        self.toc = TOCPageObject(self.driver, self.baseclass)
        self.contentpage = TitleContentPageObject(self.driver, self.baseclass)
        self.mynotes = My_Notes_Bookmark_Page(self.driver, self.baseclass)

    @allure.step("Click on Title Cover")
    def click_Title_Cover(self, category, option, sub_option, title):
        """
        Click on Title Cover
        :param category: str
        :param option: str
        :param sub_option: str
        :param title: str
        :return:
        """
        self.headerpage.click_menu()
        time.sleep(0.5)
        self.headerpage.click_menu_option(category)
        self.headerpage.click_menu_option(option)
        self.headerpage.click_menu_sub_option(sub_option)
        self.coverpage.click_title_cover(title)
