


class LoginPage:

    textbox_username_xpath="//input[@id='Email']"
    textbox_password_xpath="//input[@id='Password']"
    button_login_xpath="//input[@class='button-1 login-button']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(5)

    def SetUserName(self,username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def SetPassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
