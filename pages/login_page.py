from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .locators import DataBase as DB
from .locators import BasePageLocators as BPL
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage


class LoginPage(BasePage):

    def fill_the_login_field(self):
        self.fill_the_field(BPL.LOGIN_FIELD, DB.LOGIN)

    def fill_the_password_field(self):
        self.fill_the_field(BPL.PASSWORD_FIELD, DB.PASSWORD)

    def click_login_button(self):
        self.click_button(BPL.LOGIN_KEY)

    def fill_the_login_field_neg(self):
        self.fill_the_field(BPL.LOGIN_FIELD, DB.LOGIN_NEGATIVE)

    def fill_the_password_field_neg(self):
        self.fill_the_field(BPL.PASSWORD_FIELD, DB.PASSWORD_NEGATIVE)

    def should_be_auth_success(self):
        assert self.current_url == "https://www.saucedemo.com/inventory.html", "You have not successfully logged in"

    def should_not_be_auth_success(self):
        error_message = self.driver.find_element(*BPL.LOGIN_ERROR_MES)
        assert  error_message.text == "Epic sadface: Username and password do not match any user in this service", "You have successfully logged in"


    
    

    
