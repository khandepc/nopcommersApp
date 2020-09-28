from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SeleniumBase:

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locater_type,locater):
        if locater_type=="id":
            WebDriverWait.until(EC.presence_of_element_located(self.driver.find_element_by_id(locater)))