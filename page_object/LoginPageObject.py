import allure
from pytest_html.report import Report
from selenium.webdriver.common.by import By

from page_object.HeaderPageObject import HeaderPageObject
from selenium.webdriver.support import expected_conditions as EC


class LoginPageObject:

    def __init__(self, driver, baseclass):
        self.driver = driver
        self.baseclass = baseclass
        self.headerpage = HeaderPageObject(self.driver, self.baseclass)

    textbox_username = (By.ID, "emailAddress")
    textbox_password = (By.ID, "password")
    button_signin = (By.XPATH, "//button[@class='v-btn v-btn--block v-btn--contained theme--light v-size--large "
                               "primary']")

    @allure.step("LogIn")
    def login(self, username, password):
        """
        Enter Valid Username, Password and click Login
        :param username: str - Username text
        :param password: str - Password text
        :return: str - Subscription Type
        """
        with allure.step(f"Enter {username}"):
            self.baseclass.sendkeys(self.textbox_username, username)
        with allure.step(f"Enter {password}"):
            self.baseclass.sendkeys(self.textbox_password, password)
        with allure.step("click signin"):
            self.baseclass.click(self.button_signin)
        return self.headerpage.get_Subscription_type()
