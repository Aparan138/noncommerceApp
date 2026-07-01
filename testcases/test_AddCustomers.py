import pytest
import time

from selenium.webdriver.common.by import By

from PageObjects.AddcustomerPages import AddCustomer
from PageObjects.LoginPages import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customogger import LogGen
import string
import random

class Test_003_AddCustomers:
     baseURL=ReadConfig.getApplicationURL()
     username=ReadConfig.getUsername()
     password=ReadConfig.getPassword()
     logger=LogGen.loggen()

     @pytest.mark.sanity
     def test_addCustomer(self,setup):
         self.logger.info("*****************Test_003_AddCustomer***********")
         self.driver=setup
         self.driver.get(self.baseURL)
         self.driver.maximize_window()

         self.lp=LoginPage(self.driver)
         self.lp.setUsername(self.username)
         self.lp.setPassword(self.password)
         self.lp.clickLogin()
         self.logger.info("****** Login SuccessFull***************")

         self.logger.info("*************Starting Add Customer Test************")

         self.addcust=AddCustomer(self.driver)

         try:
             self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
             time.sleep(2)
         except:
             pass
         self.addcust.clickOnCustomerMenu()
         time.sleep(5)
         # popup close karo
         try:
             self.driver.find_element(By.XPATH, "//button[text()='Ok']").click()
             time.sleep(2)
         except:
             pass

         self.addcust.clickOnCustomersMenuItems()

         self.addcust.clickOnAddNew()

         self.logger.info("*************Providing Add new Customer Details*************")

         self.email= random_generator() + "@gmail.com"
         self.addcust.setEmail(self.email)
         self.addcust.setPassword("test123")
         self.addcust.setFirstName("Aparna")
         self.addcust.setLastName("Sharma")
         self.addcust.setGender("Female")
         self.addcust.setCompanyName("Webatlast")
         
         self.addcust.setCustomerroles("Guests")
         self.addcust.setMangerVendor("Vendor 2")
         self.addcust.setAdminContent("This is for testing......")
         self.addcust.ClickOnSave()

         self.logger.info("***** Saving Logger Info************")

         self.logger.info("******Add Customer Validation Started*******")

         self.msg=self.driver.find_element(By.TAG_NAME,"body").text
         print(self.msg)
         if 'customer has been added successfully.' in self.msg:
             assert True
             self.logger.info("******* ADD Customer Test  Passed **********")
         else:
             self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomers_src.png") #screenshots
             self.logger.info("Add Customer Test Failed*****")
             assert True == False
         self.driver.quit()
         self.driver.info("*************** Ending Home Page Title Test***********")




def random_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))