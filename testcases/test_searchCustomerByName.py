from PageObjects.SearchCustomerPage import SearchCustomer
import time
import pytest
from selenium.webdriver.common.by import By

from PageObjects.AddcustomerPages import AddCustomer
from PageObjects.LoginPages import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.logger.info("******************SearchCustomerByEmail_004**************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********* Login Sucessfully***********")

        self.logger.info("***************** Starting Search By Name *******************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomersMenuItems()

        self.logger.info("************ Searching customer by Name ***********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("victoria")
        searchcust.setLastName("Terces")
        searchcust.clickOnSearchBtnn()
        time.sleep(3)
        status=searchcust.searchCustomerByName("Victoria Terces")
        assert True==status
        self.logger.info("*********** Searching customer by Name  Finished *************")
        self.driver.close()

