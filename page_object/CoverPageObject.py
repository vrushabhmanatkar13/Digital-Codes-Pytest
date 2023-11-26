import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_object.HeaderPageObject import HeaderPageObject


class CoverPageObject:
    def __init__(self, driver, baseclass):
        self.driver = driver
        self.baseclass = baseclass

    label_pageheading = (By.XPATH, "//h1[@class='primary--text display-1']")
    label_title_names = (By.XPATH, "//div[@class='text-center col col-auto']")

    @allure.step("Page Heading")
    def get_page_heading(self):
        """
        Get Text of Page Heading
        :return: str - text of page heading.
        """
        heading: str = self.baseclass.gettext(self.label_pageheading)
        if " Building Codes" in heading:
            heading = heading.replace("Building Codes", "").strip()
        with allure.step(heading):
            return heading

    @allure.step("click {title_name}")
    def click_title_cover(self, title_name):
        """
        Click Title Cover
        :param title_name: str
        :return:
        """
        name=title_name.strip()
        title_names: list[WebElement] = self.baseclass.find_elements(self.label_title_names)
        for title in title_names:
            if title.text == name:
                self.baseclass.click_by_visibility(title)
                break
