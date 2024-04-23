from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support.ui import Select
from .locators import ProductPageLocators as PPL
from .locators import BasePageLocators as BPL
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self, locator: tuple):
        self.click_button(locator)

    def add_to_basket_first_item(self):
        self.add_to_basket(PPL.ADD_TO_BASKET_FIRST_BUT)

    # def check_the_basket_not_empty(self):
    #     assert self.get_text(PPL.SHOPING_CART_BADGE) == '1'
        
    def get_item_name(self, locator):
        self.get_text(locator)
    
    def get_products_names(self):
       return self.get_items_names(PPL.LIST_OF_ITEMS)
    
    def get_products_prices(self):
       return self.get_items_prices(PPL.LIST_OF_PRICES)

    def get_the_first_item_name(self):
        return self.get_text(PPL.FIRST_ITEM)

    def get_the_first_item_price_on_prod_page(self):
        return self.get_text(PPL.FIRST_ITEM_PRICE)
        
    def click_on_the_first_item_img(self):
        self.click_button(PPL.IMAGE_OF_FIRST_ITEM)

    def go_to_item_card(self, locator: tuple):
        self.click_button(locator)

    def go_to_first_item_page(self):
        self.go_to_item_card(PPL.FIRST_ITEM)

    def sort_items_a_to_z(self):
        menu = self.choose_element(PPL.SORT_BUTTON)
        drop_down_menu = Select(menu)
        drop_down_menu.select_by_value('az')

    def sort_items_z_to_a(self):
        menu = self.choose_element(PPL.SORT_BUTTON)
        drop_down_menu = Select(menu)
        drop_down_menu.select_by_value('za')

    def sort_items_lo_to_hi(self):
        menu = self.choose_element(PPL.SORT_BUTTON)
        drop_down_menu = Select(menu)
        drop_down_menu.select_by_value('lohi')

    def sort_items_hi_to_lo(self):
        menu = self.choose_element(PPL.SORT_BUTTON)
        drop_down_menu = Select(menu)
        drop_down_menu.select_by_value('hilo')

    def check_list_of_items_sorted_az(self, lst):
        sorted_lst = sorted(lst)
        assert lst == sorted_lst, "List are not sorted 'az'"
    
    def check_list_of_items_sorted_za(self, lst):
        sorted_lst = sorted(lst, reverse=True)
        assert lst == sorted_lst, "List are not sorted 'za'"

    def check_list_of_items_sorted_lo_hi(self, lst):
        sorted_lst = sorted(lst)
        assert lst == sorted_lst, "List are not sorted 'lo to hi'"

    def check_list_of_items_sorted_hi_lo(self, lst):
        sorted_lst = sorted(lst, reverse=True)
        assert lst == sorted_lst, "List are not sorted 'hi to lo'"


    
