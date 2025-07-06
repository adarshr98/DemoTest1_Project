import os

import pytest
from selenium import webdriver

from pytest_html import extras


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.implicitly_wait(5)
    driver.maximize_window()

    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.close()

#why request is used as an argument here- def browserInstance(request):
#First point is we are mentioning this - browser_name = request.config.getoption("browser_name") - to get the option we are requesting
#And to run the test in commandline, we should use request - like this- pytest --host-chrome - to run this, we need to use request

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.failed and not xfail) or (report.skipped and xfail):
            driver = item.funcargs.get("browserInstance")
            if driver is None:
                return

            reports_dir = os.path.join(os.path.dirname(__file__), "reports")
            os.makedirs(reports_dir, exist_ok=True)

            file_name = report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            file_path = os.path.join(reports_dir, file_name)

            _capture_screenshot(driver, file_path)

            if hasattr(report, "extra"):
                report.extra.append(extras.image(file_path))
            else:
                report.extra = [extras.image(file_path)]

def _capture_screenshot(driver, file_path):
    driver.get_screenshot_as_file(file_path)