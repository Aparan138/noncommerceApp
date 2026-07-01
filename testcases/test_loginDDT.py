import time

import pytest
from selenium import webdriver
from PageObjects.LoginPages import LoginPage
import os
from utilities.readProperties import ReadConfig
from utilities.customogger import LogGen
from utilities import XLutilities
class Test_002_DDT_Login:
    baseURL= ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"


    logger=LogGen.loggen()
    @pytest.mark.regression
    def test_login_DDT(self,setup):
        self.logger.info("***************Test 002 DDT Login")
        self.logger.info("***************Login Test Case DDT Started****************")
        self.driver =setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver) #object Creation
        self.rows=XLutilities.getRowCount(self.path,'Sheet1')
        print("Number of rows:",self.rows)

        lst_status=[]  #Empty list variable
        for r in range(2,self.rows+1):
            self.user=XLutilities.readData(self.path,'Sheet1',r,1)
            self.password=XLutilities.readData(self.path,'Sheet1',r,2)
            self.exp=XLutilities.readData(self.path,'Sheet1',r,3)


            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title

            if act_title=="Dashboard / nopCommerce administration":
                if self.exp=="Pass":
                     self.logger.info("***************Passed****************")
                     self.lp.clickLogout()
                     lst_status.append("pass")
                elif self.exp=="Fail":
                     self.logger.info("***************Failed****************")
                     self.lp.clickLogout()
                     lst_status.append("fail")
            elif act_title != "Dashboard / nopCommerce administration":
                if self.exp=="Pass":
                     self.logger.info("***************Failed****************")
                     lst_status.append("fail")
                elif self.exp=="Fail":
                    self.logger.info("********* passed")
                    lst_status.append("pass")
        if "fail"  not in lst_status:
            self.logger.info("***************DDT Passed****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("***************DDT Failed****************")
            assert False
        self.logger.info("End of Login DDT")
