import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class HeaderPageObject:
    def __init__(self, driver, baseclass):
        self.driver = driver
        self.baseclass = baseclass

    label_subscription_type = (By.XPATH, "//h4[@class='text-left']")
    label_name = (By.XPATH, "//div[@class='v-list-item__title white--text']/h4")
    label_email = (By.XPATH, "//div[@class='v-list-item__title white--text']/h5")
    button_menu = (By.XPATH, "//span[contains(text(),'Menu')]")
    menu_options = (By.XPATH, "//div[@class='v-list-item__title fs-16 font-weight-bold accent--text']")
    menu_sub_options = (By.XPATH, "//a[@class='accent--text']")

    def click_Signin(self):
        """
        Click SingIn
        :return:
        """
        with allure.step("click SignIn"):
            self.baseclass.click(self.label_subscription_type)

    def get_name_email(self):
        action: ActionChains = self.baseclass.action_chain()
        action.move_to_element(self.baseclass.wait_until(self.label_subscription_type)).perform()
        time.sleep(1)
        info = {"name": self.baseclass.gettext(self.label_name), "email": self.baseclass.gettext(self.label_email)}
        with allure.step("Name : " + info.get("name") + "/" + "email : " + info.get("email")):
            return info

    @allure.step("Subscription Type")
    def get_Subscription_type(self):
        """
        Get text of Subscription Type
        :return: str - Text of subscription type
        """
        self.baseclass.wait.until_not(EC.text_to_be_present_in_element(self.label_subscription_type, "Sign In"))
        subscription = self.baseclass.gettext(self.label_subscription_type)
        with allure.step(subscription):
            return subscription

    @allure.step("click Menu")
    def click_menu(self):
        """
        Click Menu
        :return:
        """
        self.baseclass.click(self.button_menu)

    @allure.step("click {option_text}")
    def click_menu_option(self, option_text):
        """
        Click on Menu Category
        :param option_text: str - Category text
        :return:
        """
        options: list[WebElement] = self.baseclass.find_elements(self.menu_options)
        for option in options:
            if option.text == option_text:
                self.baseclass.click_by_visibility(option)
                break

    @allure.step("click {sub_option_text}")
    def click_menu_sub_option(self, sub_option_text):
        """
        Click on Menu Sub Category
        :param sub_option_text: str - Sub Category text
        :return:
        """
        sub_options: list[WebElement] = self.baseclass.find_elements(self.menu_sub_options)
        for suboption in sub_options:
            if suboption.text == sub_option_text:
                self.baseclass.click_by_visibility(suboption)
                break
