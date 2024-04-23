from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .locators import ProductPageLocators as PPL
from .locators import BasketPageLocators as BasketPL
from .locators import BasePageLocators as BPL
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage
from faker import Faker


class BasketPage(BasePage):

    def get_the_first_item_price_on_basket_page(self):
        return self.get_text(BasketPL.FIRST_ITEM_PRICE)
    
    def get_first_item_name_on_basket_page(self):
        return self.get_text(BasketPL.FIRST_ITEM_NAME)

    def check_item_name(self, name_from_prod_page, name_grom_basket_page):
        assert name_from_prod_page == name_grom_basket_page
        
    def check_the_price(self, price_from_prod_page, price_grom_basket_page):
        assert price_from_prod_page == price_grom_basket_page

    def check_checkout_complete(self):
        assert self.get_text(BasketPL.COMPLETE_MESSAGE) == "Thank you for your order!"

    def remove_item_basket_page(self, locator: tuple):
        self.click_button(locator)

    def remove_first_item_basket_page(self):
        self.remove_item_basket_page(BasketPL.REMOVE_FIRST_ITEM_FROM_CATALOG_BUT)

    def click_checkout_button(self):
        self.click_button(BasketPL.CHECKOUT_BUTTON)

    def click_continue_button(self):
        self.click_button(BasketPL.CONTINUE_BUTTON)
    
    def click_finish_button(self):
        self.click_button(BasketPL.FINISH_BUTTON)

    def fill_checkout_form(self):
        fake = Faker()
        self.fill_the_field(BasketPL.CHECKOUT_FORM_FNAME, fake.name())
        self.fill_the_field(BasketPL.CHECKOUT_FORM_LNAME, fake.last_name())
        self.fill_the_field(BasketPL.CHECKOUT_FORM_ZIP, fake.zipcode_in_state())
        

    # def basket_is_empty(self):
    #     assert self.is_element_not_present(PPL.SHOPING_CART_BADGE), "Basket is not empty"
