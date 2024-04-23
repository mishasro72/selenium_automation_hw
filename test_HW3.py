import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from pages.locators import BasePageLocators as BPL
from pages.locators import WaitPageLocators as WPL
from pages.locators import DataBase as DB
#from pages.base_page import BasePage
from pages.wait_page import WaitPageClass
from pages.base_page import BasePage
from pages.item_page import ItemPage
import time

@pytest.mark.done
def test_the_h1_title(driver):

    page = WaitPageClass(driver, DB.BASE_URL_WAIT)
    page.open()
    page.check_the_wait_page_title()
    #time.sleep(2)

@pytest.mark.done
def test_register_new_user(driver):

    page = WaitPageClass(driver, DB.BASE_URL_WAIT)
    page.open()
    #page.check_the_loader_sign()
    page.click_on_wait_element()
    page.fill_the_login_field()
    page.fill_the_password_field()
    page.click_on_agree()
    page.click_on_registration_button()
    page.check_the_loader_sign()
    page.check_the_success_message()

@pytest.mark.done
def test_broken_image(driver):

    page = WaitPageClass(driver, DB.BASE_URL_BROKEN_IMG)
    page.open()
    page.check_for_broken_image()

@pytest.mark.current
def test_base_auth(driver):

    page = WaitPageClass(driver, DB.BASE_URL_BASE_AUTH)
    page.popup_auth_wait()
    page.check_success_basic_auth()
    #time.sleep(2)
#     page = WaitPageClass(driver, DB.BASE_URL_BASE_AUTH)
#     page.open()
#     page.wa
#     page.switch_to_alert()
#     time.sleep(2)
#    # alert.send_keys("admin" + "\t" + "admin" + "\n")
#     time.sleep(2)




