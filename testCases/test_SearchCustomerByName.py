import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestSearchCustomerByName_005:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("*********** TestSearchCustomerByName_005 **************")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("********** Login Successful **********")

        self.logger.info("********** Strating Search Customer By Name **********")
        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomersMenu()
        self.addcust.ClickOnCustomersMenuItem()

        self.logger.info("********** Search Customer By Name **********")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("victoria")
        searchcust.setLastName("Terces")
        searchcust.ClickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        assert True == status
        self.logger.info("********** TC_SearchCustomerByName_005 **********")
        self.driver.close()
