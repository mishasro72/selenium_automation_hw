import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from pages.locators import BasePageLocators as BPL
from pages.locators import ProductPageLocators as PPL
from pages.locators import DataBase as DB
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.item_page import ItemPage
import time

@pytest.mark.done
def test_authorization_poz(driver):

    page = LoginPage(driver, DB.BASE_URL)
    page.open()
    page.fill_the_login_field()
    page.fill_the_password_field()
    page.click_login_button()
    page.should_be_auth_success()

@pytest.mark.done
def test_authorization_neg(driver):

    page = LoginPage(driver, DB.BASE_URL)
    page.open()
    page.fill_the_login_field_neg()
    page.fill_the_password_field_neg()
    page.click_button(BPL.LOGIN_KEY)
    page.should_not_be_auth_success()

@pytest.mark.done
def test_add_to_basket(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.add_to_basket_first_item()
    page.check_the_basket_not_empty()

@pytest.mark.done
def test_remove_item_from_basket(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.add_to_basket_first_item()
    page.go_to_basket()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.remove_first_item_basket_page()
    basket_page.basket_is_empty()

@pytest.mark.done
def test_add_item_from_item_card(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.go_to_first_item_page()
    page.should_be_first_item_page()
    item_page = ItemPage(driver, driver.current_url)
    item_page.add_first_item_from_item_page()
    page.check_the_basket_not_empty()

@pytest.mark.done    
def test_remove_item_from_item_card(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.go_to_first_item_page()
    page.should_be_first_item_page()
    item_page = ItemPage(driver, driver.current_url)
    item_page.add_first_item_from_item_page()
    page.check_the_basket_not_empty()
    item_page.remove_item_page()
    page.basket_is_empty()

@pytest.mark.done
def test_follow_to_card_from_img(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.click_on_the_first_item_img()
    page.should_be_first_item_page()


@pytest.mark.done
def test_chechout_positive(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.add_to_basket_first_item()
    item_name = page.get_the_first_item_name()
    item_price = page.get_the_first_item_price_on_prod_page()
    page.go_to_basket()
    page.should_be_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    item_name_basket = basket_page.get_first_item_name_on_basket_page()
    item_price_basket = basket_page.get_the_first_item_price_on_basket_page()
    basket_page.check_item_name(item_name, item_name_basket)
    basket_page.check_the_price(item_price, item_price_basket)
    basket_page.check_the_basket_not_empty()
    basket_page.click_checkout_button()
    basket_page.fill_checkout_form()
    basket_page.click_continue_button()
    basket_page.click_finish_button()
    basket_page.check_checkout_complete()

@pytest.mark.done
def test_sort_az(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    # menu = page.choose_element(PPL.SORT_BUTTON)
    # drop_down_menu = Select(menu)
    # drop_down_menu.select_by_value('za')
    page.sort_items_a_to_z()
    #print(page.get_items_names(PPL.LIST_OF_ITEMS))
    lst = page.get_products_names()
    page.check_list_of_items_sorted_az(lst)

@pytest.mark.done
def test_sort_za(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.sort_items_z_to_a()
    #print(page.get_items_names(PPL.LIST_OF_ITEMS))
    lst = page.get_products_names()
    page.check_list_of_items_sorted_za(lst)

@pytest.mark.done
def test_sort_lo_to_hi(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.sort_items_lo_to_hi()
    lst = page.get_products_prices()
    page.check_list_of_items_sorted_lo_hi(lst)

@pytest.mark.current
def test_sort_hi_to_lo(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.sort_items_hi_to_lo()
    lst = page.get_products_prices()
    page.check_list_of_items_sorted_hi_lo(lst)
    #time.sleep(2)

@pytest.mark.done
def test_burger_logout(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.burger_menu_logout()
    page.should_be_base_url_page()

@pytest.mark.done
def test_burger_about(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.burger_menu_about()
    page.should_be_about_page()

@pytest.mark.done
def test_burger_rest_app(driver, authorization):

    page = ProductPage(driver, DB.BASE_URL)
    page.add_to_basket_first_item()
   # time.sleep(2)
    page.check_the_basket_not_empty()
    page.burger_menu_rest_app()
    page.basket_is_empty()
    time.sleep(2)











#     driver.find_element(*ADD_TO_BASKET_FIRST_BUT).click()
#     assert driver.find_element(*SHOPING_CART_BADGE).text == '1'



#     driver.get(BASE_URL)

#     driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
#     driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
#     driver.find_element(*LOGIN_KEY).click()

#     assert driver.current_url == "https://www.saucedemo.com/inventory.html"

# BASE_URL = 'https://www.saucedemo.com/'

# #locators
# LOGIN_FIELD = (By.XPATH, '//*[@id="user-name"]')
# PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
# LOGIN_KEY = (By.XPATH, '//*[@id="login-button"]')

# #data
# LOGIN = 'standard_user'
# PASSWORD = 'secret_sauce'

#authorization tests 
# @pytest.mark.positive
# def test_authorize_poz(driver):

#     driver.get(BASE_URL)

#     driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
#     driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
#     driver.find_element(*LOGIN_KEY).click()

#     assert driver.current_url == "https://www.saucedemo.com/inventory.html"

# @pytest.mark.negative
# def test_authorize_neg(driver):

#     driver.get(BASE_URL)
#     driver.find_element(*LOGIN_FIELD).send_keys(LOGIN_NEGATIVE)
#     driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_NEGATIVE)
#     driver.find_element(*LOGIN_KEY).click()
    
#     error_message = driver.find_element(*LOGIN_ERROR_MES)
#     #print(error_message.text)
#     assert  error_message.text == "Epic sadface: Username and password do not match any user in this service"

# #basket test

# @pytest.mark.positive
# @pytest.mark.basket
# def test_add_to_basket(driver, authorization):

#     driver.find_element(*ADD_TO_BASKET_FIRST_BUT).click()
#     assert driver.find_element(*SHOPING_CART_BADGE).text == '1'

# @pytest.mark.positive
# @pytest.mark.basket
# def test_remove_item_from_basket(driver, authorization):











