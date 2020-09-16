

class ManufacturePage:

    catelog_link_xpath="//div[@class='main-sidebar']/div/ul/li/a/span[contains(text(),'Catalog')]"
    manufactures_link_xpath="//ul[@class='treeview-menu']/li/a/span[contains(text(),'Manufacturers')]"
    add_new_button_link_xpath="//div[@class='pull-right']/a"
    text_box_name_xpath="//input[@id='Name']"
    button_save_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)


    def click_on_cateloge(self):
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

