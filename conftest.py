import os
import warnings

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from utilities.file_utils import FileUtils


def config_location():
    if "VIRTUAL_ENV" in os.environ:
        return f"{os.getenv('VIRTUAL_ENV')}/.."
    else:
        return os.getcwd()


BROWSERS = ["chrome", "edge", "firefox"]
ENVIRONMENT_PATH = f"{config_location()}/environment.yaml"
_driver = None


@pytest.fixture
def browser(pytestconfig):
    return pytestconfig.getoption("browser", default="chrome").lower()


@pytest.fixture
def ambiente(pytestconfig):
    return pytestconfig.getoption("env", default="test").lower()


@pytest.fixture
def env(request):
    _env = FileUtils.get_yaml_data(ENVIRONMENT_PATH)
    if request.cls is not None:
        request.cls.env = _env
    return _env


def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        if metafunc.config.getoption("--browser") == "all":
            metafunc.parametrize("browser", BROWSERS)
        else:
            metafunc.parametrize("browser", metafunc.config.getoption("--browser").split(","))


def pytest_addoption(parser):
    parser.addoption("-B", "--browser", dest="browser", action="store", default="chrome",
                     choices=['chrome', 'firefox', 'edge', 'all'])
    parser.addoption("--env", dest="env", action="store", default="test")


def pytest_exception_interact(node, report):
    try:
        if node.funcargs['driver'] is not None and report.failed:
            _driver.execute_script("document.body.bgColor = 'white';")
            allure.attach(_driver.get_screenshot_as_png(), name=node.name, attachment_type=AttachmentType.PNG)
    except Exception as e:
        warnings.warn(f"No se pudo adjuntar la imagen. Error: {e}")


@allure.step('Enter the site')
@pytest.fixture
def driver(request, browser, env, ambiente):
    '''
    “Yield” fixtures yield instead of return. Thus, we can run some code and pass an object back to the requesting
    fixture/test, and any teardown code for that fixture is placed after the yield.
    '''
    global _driver
    _driver = get_driver(browser)
    _driver.implicitly_wait(30)
    _driver.get(env[ambiente]['url'])
    _driver.maximize_window()
    if request.cls is not None:
        request.cls.driver = _driver
    yield _driver
    close_browser()
    quit_driver()


@allure.step("Close browser")
def close_browser():
    _driver.close()


@allure.step("Quit driver")
def quit_driver():
    _driver.quit()


def driver_broker(browser):
    return {
        "chrome": (webdriver.Chrome, ChromeDriverManager, ChromeService, ChromeOptions),
        "firefox": (webdriver.Firefox, GeckoDriverManager, FirefoxService, FirefoxOptions),
        "edge": (webdriver.Edge, EdgeChromiumDriverManager, EdgeService, EdgeOptions)
    }[browser]


@allure.step(f'Search compatible {browser} driver')
def get_driver(browser):
    """
    Returns a previously configured driver. Browser Service installs the driver, updated to the latest version
    available and compatible with the installed browser.
    """
    try:
        driver_class, driver_manager, service_class, options_class = driver_broker(browser)
        path = driver_manager().install()
        service = service_class(executable_path=path)
        options = options_class()
        options.accept_insecure_certs = True
        web_driver = driver_class(service=service, options=options)
        return web_driver
    except RuntimeError as e:
        raise RuntimeError(f"{browser}: Tipo de browser no conocido", e)
