import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUties

class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********************* Test_002_DDT_Login ************************")
        self.logger.info("********************* Verifying login DDT test **********************")
        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        self.rows=XLUties.getRowCount(self.path,"Sheet1")
        print("number of rows in a Excel: ",self.rows)

        lst_status=[] #Empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUties.readData(self.path,"Sheet1",r,1)
            self.password=XLUties.readData(self.path,"Sheet1",r,2)
            self.exp=XLUties.readData(self.path,"Sheet1",r,3)

            self.lp.SetUserName(self.user)
            self.lp.SetPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.ClickLogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.ClickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test Failed ***")
            self.driver.close()
            assert False
        self.logger.info("******************** End of login DDT test ***************************")
        self.logger.info("********************* completed TC_Login_DDT_002 ***********************")