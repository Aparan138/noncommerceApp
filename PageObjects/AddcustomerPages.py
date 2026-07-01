import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    #add customer page
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath="//p[text()=' Customers']/ancestor::a"
    btnAddnew_xpath="//a[normalize-space()='Add new']"
    txtEmail_Xpath="//input[@id='Email']"
    txtPassword_Xpath="//input[@id='Password']"
    txtCustomerroles_Xpath="//ul[@class='select2-selection__rendered']"
    listitemAdministrators_Xpath="//li[contains(text(),'Administrators')]"
    listitemRegistered_Xpath="//li[@id='select2-SelectedCustomerRoleIds-result-f7pe-3']"
    listitemGuests_Xpath="//li[@id='select2-SelectedCustomerRoleIds-result-gxp8-4']"
    listitemVendors_Xpath="//span[@id='select2-VendorId-container']"
    drpmgrofVendors_Xpath="//*[@id='VendorId']"
    rdMaleGenders_Xpath="//input[@id='Gender_Male']"
    rdFemaleGenders_Xpath="//input[@id='Gender_Female']"
    txtFirstName_Xpath="//input[@id='FirstName']"
    txtLastName_Xpath="//input[@id='LastName']"
    txtCompanyName_Xpath="//input[@id='Company']"
    txtAdminContent_Xpath="//textarea[@id='AdminComment']"
    btnSave_Xpath="//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItems(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_Xpath).send_keys(email)

    def setPassword(self,Password):
        self.driver.find_element(By.XPATH,self.txtPassword_Xpath).send_keys(Password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtFirstName_Xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txtLastName_Xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.rdMaleGenders_Xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.rdFemaleGenders_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rdMaleGenders_Xpath).click()

    def setCompanyName(self,comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_Xpath).send_keys(comname)

    def setCustomerroles(self,role):
        self.driver.find_element(By.XPATH,self.txtCustomerroles_Xpath).click()
        time.sleep(3)
        if role=='Registered':
         self.listitem=self.driver.find_element(By.XPATH,self.listitemRegistered_Xpath)
        elif role=='Administrators':
         self.listitem=self.driver.find_element(By.XPATH,self.listitemAdministrators_Xpath)
        elif role=='Guests':
            #Here user can be Registered(or)Guest,only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//span[@role='presentation'][normalize-space()='×']")
            self.listitem=self.driver.find_element(By.XPATH,self.listitemGuests_Xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.listitemVendors_Xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.listitemRegistered_Xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.listitemGuests_Xpath)
        time.sleep(3)
        #self.listitem.click() soetimes click action not perform on variable so we have to implement javascript statement
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setMangerVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrofVendors_Xpath))
        drp.select_by_value(value)
    def setAdminContent(self,comment):
        self.driver.find_element(By.XPATH,self.txtAdminContent_Xpath).send_keys(comment)
    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_Xpath).click()




