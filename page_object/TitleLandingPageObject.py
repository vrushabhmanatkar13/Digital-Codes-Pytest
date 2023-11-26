import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TitleLandingPageObject:

    def __init__(self, driver, baseclass):
        self.driver = driver
        self.baseclass = baseclass

    label_title_name = (By.XPATH, "//h1[@class='font-weight-regular']")
    label_title_tag = (By.XPATH, "//h1[@class='font-weight-regular']/span")
    label_start_free = (By.XPATH, "//span[@class='roboto caption']")
    label_active_premium = (By.XPATH, "//p[@class='mb-0 primary--text']")
    chip_category = (By.XPATH, "(//a/span[@class='v-chip__content'])[1]")
    current_viewing = (By.XPATH, "//div[@class='v-select__selections']/p")
    current_version = (By.XPATH, "//div[@aria-selected='true']//div[@class='col']")
    old_version = (By.XPATH, "(//div[@aria-selected='false']//div[@class='col'])[1]")

    @allure.step("Get Title Name")
    def get_title_name(self):
        """
        Get text of Title Name on Title Landing Page
        :return: str - Text of title name
        """
        element: WebElement = self.baseclass.find(self.label_title_name)
        child = element.find_element(by=By.TAG_NAME, value="span")
        title = self.baseclass.gettext_by_visibility(element).replace(child.text, "").strip()
        with allure.step(title):
            return title

    @allure.step("Get Title Tag")
    def get_title_tag(self):
        """
        Get text of Title Tag Name on Title Landing Page
        :return: str - Text of tag name
        """
        tag = self.baseclass.gettext(self.label_title_tag)
        with allure.step(tag):
            return tag

    @allure.step("Get text of Start Trial for {subscription_type}")
    def get_Start_Trial_text(self, subscription_type):
        """
        Get Start Trial Text on Title Landing Page
        :param subscription_type: str - Subscription Type
        :return: str - Text of Start Trial
        """
        if subscription_type != "Premium Complete":
            text = self.baseclass.gettext(self.label_start_free)
            with allure.step(text):
                return text
        else:
            return ""

    @allure.step("Get Active Premium Text for {tag_name}")
    def get_active_premium_text(self, tag_name):
        """
        Get Active Premium Text on Title Landing Page
        :param tag_name: str - Title tag name
        :return: str - Active Premium Text
        """
        if tag_name == "PREMIUM":
            text = self.baseclass.gettext(self.label_active_premium)
            with allure.step(text):
                return text
        else:
            return ""

    @allure.step("Get Category")
    def get_first_category(self):
        """
        Get first Category text on Title Landing Page
        :return: str - Category Text
        """
        text = self.baseclass.gettext(self.chip_category)
        with allure.step(text):
            return text

    @allure.step("Verify Current Version")
    def verify_current_version(self):
        """
        To Verify Current Version of Title
        :return:
        """
        current_viewing = self.baseclass.gettext(self.current_viewing)
        with allure.step(f"Current version: {current_viewing}"):
            self.baseclass.click(self.current_viewing)
            current_version = self.baseclass.gettext(self.current_version)
            if current_viewing == current_version:
                return True
            else:
                raise Exception(f"Current viewing: {current_viewing} not match to current version: {current_version}")

    @allure.step("Change Version")
    def change_version(self):
        """
        Change Version of Title
        :return:
        """
        old_version = self.baseclass.gettext(self.old_version)
        with allure.step(f"Change Version to: {old_version}"):
            self.baseclass.click(self.old_version)
        current_viewing = self.baseclass.gettext(self.current_viewing)
        if old_version == current_viewing:
            return True
        else:
            raise Exception(f"Current viewing: {current_viewing} not match to {old_version}")
