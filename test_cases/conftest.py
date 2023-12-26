import os
import platform

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utiilites.Logger import set_logger
from utiilites.readProperties import getConfig

config = getConfig("./Configuration/config.ini")
implicit_wait = float(config.get('waits', 'implicit_wait'))
zoom = config.get('zoom', 'value')



def pytest_addoption(parser):
    """
    for select browser Name and Headless mode
    :param parser:
    :return: None
    """
    parser.addoption(
        "--browsername", action="store", default="chrome"
    )
    parser.addoption(
        "--headless", action="store_true", default=False
    )
    parser.addoption(
        "--env", action="store", default=""
    )


@allure.title("Setup Log file")
@pytest.fixture(scope="session", autouse=True)
def Set_log_file():
    """
    Execute before Session to Set up Log file
    :return: None
    """
    file = "./Logs/logfile.log"
    if os.path.exists(file):
        os.remove(file)
    yield set_logger(file)


@allure.title("Get Enviroment url")
@pytest.fixture(scope="package", autouse=True)
def get_Environment(request):
    environment = request.config.getoption("--env")
    global url
    if environment == None:
        url = config.get('url', environment)
    else:
        url = config.get('url', 'stage')
    return url


@allure.title("Setup Browser and Tear Down")
@pytest.fixture(scope="class", autouse=True)
def Setup_TearDown(request):
    """
     Execute before class to Set up Browser, Implicit wait and pass url
    :param request:
    :return: Webdriver
    """
    global driver
    browser_name: [str] = request.config.getoption("--browsername")
    # get_Environment(request)
    if browser_name.lower() == "chrome":
        driver = Chrome_Option(request)
    elif browser_name.lower() == "firefox":
        driver = Firefox_Option(request)
    elif browser_name.lower() == "edge":
        driver = Edge_Option(request)
    else:
        raise Exception("Browser not Present")
    with allure.step(f"Platform Info :{platform.platform()}"):
        pass
    with allure.step(f"Python Version :{platform.python_version()}"):
        pass
    with allure.step(f"Browser Name :{driver.name}"):
        pass
    with allure.step(f"Url-Environment :{url}"):
        pass
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(implicit_wait)
    request.cls.driver = driver
    yield driver
    driver.quit()


@allure.title("Get Result of Test")
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    To get status of test cases
    :param item:
    :param call:
    :return: result of hook impl
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@allure.title("Take ScreenShot on failure")
@pytest.fixture(autouse=True)
def log_on_failure(request):
    """
    To attach screenshot in allure report when any test case is failed
    :param request:
    :return:
    """
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name=request.node.name,
                      attachment_type=allure.attachment_type.PNG)


# @pytest.fixture(scope="class", autouse=True)
# def set_driver_variable(request, Setup_TearDown):
#     """
#     Execute before class to set driver variable
#     :param request:
#     :param Setup_TearDown:
#     :return:
#     """
#     request.cls.driver = Setup_TearDown


def Chrome_Option(request):
    """
    To Set Chrome Options capabilities
    :param request:
    :return: WebDriver
    """
    headless_mode = request.config.getoption("--headless")
    option = webdriver.ChromeOptions()
    if headless_mode:
        option.add_argument("headless")

    option.accept_insecure_certs = True
    option.add_argument("–incognito")
    option.add_argument(f"--force-device-scale-factor={zoom}")
    driver = webdriver.Chrome(service=Service(), options=option)
    return driver


def Firefox_Option(request):
    """
    To Set Firefox Options capabilities
    :param request:
    :return: WebDriver
    """
    headless_mode = request.config.getoption("--headless")
    option = webdriver.FirefoxOptions()
    if headless_mode:
        option.add_argument("-headless")
    option.accept_insecure_certs = True
    option.add_argument("-private-window")
    option.add_argument(f"--force-device-scale-factor={zoom}")
    driver = webdriver.Firefox(service=Service(), options=option)
    return driver


def Edge_Option(request):
    """
    To Set Edge Options capabilities
    :param request:
    :return: WebDriver
    """
    headless_mode = request.config.getoption("--headless")
    option = webdriver.EdgeOptions()
    if headless_mode:
        option.add_argument("headless")
    option.accept_insecure_certs = True
    option.add_argument("–incognito")
    driver = webdriver.Edge(service=Service(), options=option)
    return driver
