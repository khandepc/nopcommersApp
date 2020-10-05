from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen

class SeleniumBase:

    logger=LogGen.loggen()

    def __init__(self,driver):
        self.driver=driver

    def find_element(self,locater_type,locater):
        if locater_type=="id":
            return WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.ID,locater)))
        elif locater_type=="name":
            return WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.NAME,locater)))
        elif locater_type=="classname":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, locater)))
        elif locater_type=="tagname":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, locater)))
        elif locater_type=="linktext":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, locater)))
        elif locater_type=="partiallinktext":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locater)))
        elif locater_type=="css":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, locater)))
        elif locater_type=="xpath":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, locater)))
        else:
            self.logger.error("Invalid locater type")


    def find_elements(self, locater_type, locater):

        if locater_type == "id":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.ID, locater)))
        elif locater_type == "name":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.NAME, locater)))
        elif locater_type == "classname":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, locater)))
        elif locater_type == "tagname":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, locater)))
        elif locater_type == "linktext":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.LINK_TEXT, locater)))
        elif locater_type == "partiallinktext":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, locater)))
        elif locater_type == "css":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locater)))
        elif locater_type == "xpath":
            return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, locater)))
        else:
            self.logger.error("Invalid locater type")
