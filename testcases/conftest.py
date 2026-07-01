from selenium import webdriver
import pytest
@pytest.fixture
def setup(browser):
        if browser=='chrome':
          driver = webdriver.Chrome()
          print("launching chrome browser...............")
        elif browser=='firefox':
          driver=webdriver.Firefox()
          print("launching firefox browser...............")
        else:
          driver=webdriver.Ie()  #This will take default browser
        return driver

def pytest_addoption(parser): #This will get the value from CLI
        parser.addoption("--browser", action="store")

@pytest.fixture
def browser(request): #this will return the Browser value to setup Method
        return request.config.getoption("--browser")

####################Pytest HTML Reports##################################
#Its is hook for adding Enviroment info to HTML Report
from pytest_metadata.plugin import metadata_key as pytest_metadata_key

def pytest_configure(config):
    config.stash[pytest_metadata_key]["Project Name"] = "nop Commerce"
    config.stash[pytest_metadata_key]["Module Name"] = "Customer"
    config.stash[pytest_metadata_key]["Tester"] = "Radha"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)