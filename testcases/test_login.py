import pytest
from selenium import webdriver
from PageObjects.LoginPages import LoginPage
import os
from utilities.readProperties import ReadConfig
from utilities.customogger import LogGen
class Test_001_Login:
    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("***************Test_001_Login****************")
        self.logger.info("***************Verifying Home Page Title****************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="nopCommerce demo store. Login":
            self.logger.info("***************HomePge Title Test is Passed****************")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_homePageTitle.png")
            self.logger.info("***************HomePge Title Test is Failed****************")
            assert False
        self.driver.quit()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***************Login Test Case Started****************")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver) #object Creation
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************Login Test Case Passed****************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_login.png")
            assert False
        self.driver.quit()