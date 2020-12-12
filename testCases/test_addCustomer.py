import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("--- URL Entered")

        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.logger.info("--- Username Entered :"+self.username)
        self.lp.SetPassword(self.password)
        self.logger.info("--- Password Entered :"+self.password)
        self.lp.ClickLogin()
        self.logger.info("--- clicked on login")
        self.logger.info("*************** Login Successful ****************")

        self.logger.info("*************** Starting Add Customer Test ************")
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.logger.info("--- clicked on Customers Menu")
        self.addcust.ClickOnCustomersMenuItem()
        self.logger.info("--- clicked on Customers Menu Item")
        self.addcust.ClickOnAddnew()
        self.logger.info("--- clicked on Add New")

        self.logger.info("*********** Providing customer info ************")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Prashant")
        self.addcust.setLastname("Khande")
        self.addcust.setGender("Male")
        self.addcust.setDob("4/09/1996")  # Format : D/MM/YYYY
        self.addcust.setCompantName("KWPL")
        #self.addcust.setNewsletter()
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerofVendor('Vendor 2')
        self.addcust.setAdminContent("This is foe testing...")
        self.addcust.ClickOnSave()
        self.logger.info("*********** Saving customer info *************")

        self.logger.info("*********** Add customer validation Started **********")
        self.msg = self.driver.find_element_by_tag_name("body").text

        #print(self.msg)
        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********** Add customer test Passed **********")
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") # Screenshot
            self.logger.error("********** Add Customer Test Failed **********")
            self.driver.close()
            assert True == False

        self.driver.close()
        self.logger.info("********** Ending Test_003_AddCustomer *************")
# this function created for generating random email

def random_generator(size=8,chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars)for x in range(size))
