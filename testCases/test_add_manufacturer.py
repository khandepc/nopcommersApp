
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddManufacturPage import ManufacturePage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_006_AddManifacturer:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
    manufacturer_name="Khande works private limited"

    @pytest.mark.sanity
    def test_add_manufacturer(self,setup):
        self.logger.info("********** Test_006_AddManifacturer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("--- URL Entered Successfully")
        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.logger.info("--- user name Entered :"+self.username)
        self.lp.SetPassword(self.password)
        self.logger.info("--- password Entered :"+self.password)
        self.lp.ClickLogin()
        self.logger.info("--- clicked on login")
        self.logger.info('********** login successfull **********')

        self.logger.info("********** Stating Add Manufacturer Test **********")
        self.addManufacture=ManufacturePage(self.driver)
        self.addManufacture.click_on_cateloge()
        self.logger.info("--- clicked on cateloge")
        self.addManufacture.click_on_manufacture()
        self.logger.info("--- clicked on manufacturer")
        self.addManufacture.click_on_add_nuw_button()
        self.logger.info("--- clicked on Add new button")

        self.logger.info("********** Entering manufacturer name **********")
        self.addManufacture.set_name_of_manufacturer(self.manufacturer_name)
        self.logger.info("--- Manufacturer name Entered :"+self.manufacturer_name)
        self.addManufacture.click_on_save_button()
        self.logger.info("--- clicked on save button")
        self.logger.info("********** saving manufacturer **********")

        self.logger.info("********** Add manufacturer validation started **********")
        self.actual_msg=self.driver.find_element_by_tag_name("body").text
        self.expected_msg = "The new manufacturer has been added successfully."

        if self.expected_msg in self.actual_msg:
            assert True==True
            self.logger.info("********** Add manufacturer Test Passed **********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addmanufacturer_scr.png")
            self.logger.error("********** Add Manufacturer Test Failed **********")
            assert True == False

        self.driver.close()
        self.logger.info("********** Ending Test_006_AddManifacturer **********")