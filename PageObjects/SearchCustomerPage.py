from selenium.webdriver.common.by import By


class SearchCustomer:
    txtEmail_id="SearchEmail"
    txtFirstName="SearchFirstName"
    txtLastName="SearchLastName"
    btnSearch_id="search-customers"


    tblSearchResult_xpath="//table[@id='customers-grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableCols_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)
    def setFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFirstName).clear()
        self.driver.find_element(By.ID,self.txtFirstName).send_keys(fname)
    def setLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLastName).clear()
        self.driver.find_element(By.ID,self.txtLastName).send_keys(lname)
    def clickOnSearchBtnn(self):
        self.driver.find_element(By.XPATH,self.btnSearch_id).click()
    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tblSearchResult_xpath))
    def getNoOfCols(self):
        return len(self.driver.find_elements(By.XPATH,self.tblSearchResult_xpath))
    def searchCustomerByEmail(self,email):
        flag=False
        for r in (1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid ==email:
                flag=True
                break
            return flag
    def searchCustomerByName(self,Name):
        flag=False
        for r in (1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            name=table.find_element(By.XPATH,"//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
            return flag

