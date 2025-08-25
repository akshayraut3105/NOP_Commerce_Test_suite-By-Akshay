import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Browser...")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox Browser...")
    else:
        raise ValueError(f"Browser '{browser}' is not supported.")

    driver.maximize_window()

    # yield instead of return so teardown can run
    yield driver

    print("Closing browser...")
    driver.quit()   # test khatam hone ke baad close


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser option: chrome or firefox")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
 #

 #lets create code to get information about html report and project
# -------- Report Customization ----------
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "NOP Commerce Automation Report"

@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    # pytest-metadata plugin required
    if not hasattr(config, "_metadata"):
        config._metadata = {}
    config._metadata["Project Name"] = "NOP Commerce"
    config._metadata["Module"] = "Login"
    config._metadata["Tester"] = "Akshay Raut"