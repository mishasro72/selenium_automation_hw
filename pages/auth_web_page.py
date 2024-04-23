from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .locators import AuthWebPageLocators as AWPL
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement

class AuthWebPage (BasePage):
 #   def __init__(self, *args, **kwargs):
  #      super(AuthWebPage, self).__init__(*args, **kwargs)

    def element_should_be_disable(self, locator):
        assert self.is_element_disabled(locator) == True

    def element_should_be_enable(self, locator):
        assert self.is_element_disabled(locator) == False


