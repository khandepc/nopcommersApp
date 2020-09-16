
from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(executable_path="C:\\Users\\chand\\Downloads\\chromedriver_version_83_win32\\chromedriver.exe")
        driver.maximize_window()
        print("launching chrome browser..............")
    elif browser=="firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\chand\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe")
        driver.maximize_window()
        print("launching firefox browser..............")
    elif browser=="ie":
        driver = webdriver.Chrome(executable_path="C:\\Users\\chand\\Downloads\\chromedriver_version_83_win32\\chromedriver.exe")
        driver.maximize_window()
        print("launching IE browser..............")
    else:
        driver = webdriver.Chrome(executable_path="C:\\Users\\chand\\Downloads\\chromedriver_version_83_win32\\chromedriver.exe")
        print("launching chrome browser bydefault..............")
        driver.maximize_window()
    return driver

def pytest_addoption(parser): #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

############## pytest HTML Report ####################

# it is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"]="nop Commerce"
    config._metadata["Module Name"]="Customers"
    config._metadata["Tester"]="Prashant Khande"

# it is hook for delete / modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)