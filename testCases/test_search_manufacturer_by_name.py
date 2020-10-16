
import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddManufacturPage import ManufacturePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_search_manufacturere_by_name_007:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()


    def test_search_manufacturer_by_name(self,setup):
        self.logger.info("******Test_search_manufacturere_by_name_007 ******")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("****** Login successfull ******")

        self.logger.info("****** search manufacturer by name started ******")
        self.mp=ManufacturePage(self.driver)
        self.mp.click_on_cateloge()
        self.mp.click_on_manufacture()
        self.mp.search_manufacturer_name("khande works")
        self.mp.click_on_search_button()

        self.logger.info("****** Search manufacturer by name Validation start ******")

        actual_result=self.driver.find_element_by_xpath("//*[@id='manufacturers-grid']/tbody/tr[1]/td[2]").text
        expected_result="khande works"
        if expected_result in actual_result:
            assert True
            self.logger.info("actual result is "+actual_result)
            self.logger.info("****** Search manufacturer test passed ******")
        else:
            self.logger.error("****** Search manufacturer test failed ******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Search_manufacturer_scr.png")
            assert False
        self.driver.close()
        self.logger.info("****** Ending Test_search_manufacturere_by_name_007 ******")