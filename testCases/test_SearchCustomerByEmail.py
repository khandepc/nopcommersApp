import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestSearchCustomerByEmail_004:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*********** SearchCustomerByEmail_004 **************")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Strating Search Customer By Email **********")
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.logger.info("********** Search Customer By EmailID **********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.ClickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("********** TC_SearchCustomerByEmail_004 Finished **********")
        self.driver.close()
