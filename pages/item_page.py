from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .locators import ProductPageLocators as PPL
from .locators import BasketPageLocators as BasketPL
from .locators import ItemPageLocators as IPL
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement
from .product_page import ProductPage

class ItemPage(ProductPage):

    def add_first_item_from_item_page(self):
        self.add_to_basket(IPL.ADD_TO_CART_BUT)

    def remove_item_page(self):
        self.click_button(IPL.REMOVE_ITEM_BUT)



