
class SearchCustomer():
    #Add customer page
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tableSearchRusults_xpath = "//table[@role='grid']"
    table_xpath = "//*[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txtLastName_id)
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNumOfRows(self):
        lenth_of_rows=len(self.driver.find_elements_by_xpath(self.tableRows_xpath))
        return lenth_of_rows

    def getNumOfColumn(self):
        length_of_columns=len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))
        return length_of_columns

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNumOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            emailid=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email==emailid:
                flag = True
                break

        return flag

    def searchCustomerByName(self,name):
        flag = False
        for r in range(1,self.getNumOfRows()+1):
            table=self.driver.find_element_by_xpath(self.table_xpath)
            fname=table.find_element_by_xpath("//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name==fname:
                flag=True
                break
        return flag