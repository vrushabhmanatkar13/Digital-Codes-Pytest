import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from test_cases.conftest import config
from utiilites.Logger import get_logger
from selenium.webdriver.support import expected_conditions as EC

webdriver_wait = float(config.get('waits', 'webdriver_wait'))


class BaseClass:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, webdriver_wait)

    def find(self, locator):
        log = get_logger("find_element")
        try:
            return self.driver.find_element(by=locator[0], value=locator[1])
        except Exception as e:
            log.error(f"Element Not Found {locator}" + str(e).splitlines()[1])

    def find_elements(self, locator):
        log = get_logger("find_elements")
        try:
            elements: list[WebElement] = self.wait.until(EC.visibility_of_any_elements_located(locator))
            return elements
        except Exception as e:
            log.error("Element Not Found " + str(e).splitlines()[1])

    def wait_title_is(self, title):
        return self.wait.until(EC.title_is(title))

    def wait_until(self, locator):
        log = get_logger("isDisplay")
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            log.error("Element Not Found " + str(e).splitlines()[0])

    def click(self, locator):
        log = get_logger("click")
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).click()
            log.info(f"click : {locator}")
        except Exception as e:
            log.error("Element Not Found " + str(e).splitlines()[0])

    def click_by_visibility(self, web_element):
        log = get_logger("click_by_visibility")
        try:
            self.wait.until(EC.visibility_of(web_element)).click()
            log.info(f"click : {web_element}")
        except Exception as e:
            log.error("Element Not Found " + str(e).splitlines()[0])

    def click_javascript(self, web_element):
        log = get_logger("click_javascript")
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located(web_element))
            self.driver.execute_script("arguments[0].click();", element)
            log.info(f"click : {web_element}")
        except Exception as e:
            log.error("Element Not Found" + str(e).splitlines()[0])

    def sendkeys(self, locator, value):
        log = get_logger("sendkeys")
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(value)
            log.info(f"send keys : {locator}, value : {value}")
        except Exception as e:
            log.error("Element Not found" + str(e).splitlines()[0])

    def gettext(self, locator):
        log = get_logger("gettext")
        try:
            element: WebElement = self.wait.until(EC.visibility_of_element_located(locator))
            log.info(f"get text : {locator}, value : {element.text}")
            return element.text
        except Exception as e:
            log.error("Element Not found" + str(e).splitlines()[0])

    def gettext_by_visibility(self, web_element):
        log = get_logger("gettext_by_visibility")
        try:
            element: WebElement = self.wait.until(EC.visibility_of(web_element))
            log.info(f"get text : {web_element}, value : {element.text}")
            return element.text
        except Exception as e:
            log.error("Element Not found" + str(e).splitlines()[0])

    def action_chain(self):
        action = ActionChains(self.driver)
        return action

    @staticmethod
    def assert_equals(Expected, Actual, test_logger: logging.Logger):
        assert Expected == Actual, (
            test_logger.error(f"Expected: {Expected}, Found: {Actual}")

        )

    @staticmethod
    def assert_not_equals(Expected, Actual, test_logger: logging.Logger):
        assert Expected != Actual, (
            test_logger.error(f"Expected: {Expected}, Found: {Actual}")
        )

    @staticmethod
    def assert_True(Actual: bool, test_logger: logging.Logger):
        assert Actual, (
            test_logger.error(f"Expected: True, Found: {Actual} ")
        )

    @staticmethod
    def assert_False(Actual: bool, test_logger: logging.Logger):
        assert not Actual, (
            test_logger.error(f"Expected: False, Found: {Actual} ")
        )
