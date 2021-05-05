from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from selenium.common.exceptions import TimeoutException
from Pages.HomePage import HomePage





class LoginPage(BasePage):
    """By Locators"""
    EMAIL = (By.ID,"username")
    PASSWORD = (By.ID,"password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT,"Sign up")


    """Constructor of Page Class"""
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """this is used to get page title"""

    def get_login_page_title(self,title):
        return self.get_title(title)

    """this is used to check signup link"""

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """This is used to login to app"""
    def do_login(self,username,password):
        self.do_send_keys(self.EMAIL,username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)


