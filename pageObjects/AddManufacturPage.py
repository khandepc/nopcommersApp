from utilities.seleniumBase import SeleniumBase

class ManufacturePage:

    catelog_link_xpath="//div[@class='main-sidebar']/div/ul/li/a/span[contains(text(),'Catalog')]"
    manufactures_link_xpath="//ul[@class='treeview-menu']/li/a/span[contains(text(),'Manufacturers')]"
    add_new_button_link_xpath="//div[@class='pull-right']/a"
    text_box_name_xpath="//input[@id='Name']"
    button_save_xpath="//button[@name='save']"
    manufacturer_name_input_box_xpath="//input[@id='SearchManufacturerName']"
    search_button_xpath="//button[@id='search-manufacturers']"



    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)


    def click_on_cateloge(self):
        sb=SeleniumBase(self.driver)
        self.driver.find_element_by_xpath(self.catelog_link_xpath).click()

    def click_on_manufacture(self):
        self.driver.find_element_by_xpath(self.manufactures_link_xpath).click()

    def click_on_add_nuw_button(self):
        self.driver.find_element_by_xpath(self.add_new_button_link_xpath).click()

    def set_name_of_manufacturer(self,name):
        self.driver.find_element_by_xpath(self.text_box_name_xpath).clear()
        self.driver.find_element_by_xpath(self.text_box_name_xpath).send_keys(name)

    def click_on_save_button(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()

    def search_manufacturer_name(self,name):
        self.driver.find_element_by_xpath(self.manufacturer_name_input_box_xpath).clear()
        self.driver.find_element_by_xpath(self.manufacturer_name_input_box_xpath).send_keys(name)

    def click_on_search_button(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()


