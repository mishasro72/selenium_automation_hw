import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from pages.locators import BasePageLocators as BPL
from pages.locators import AuthWebPageLocators as AWPL
from pages.locators import DataBase as DB
#from pages.base_page import BasePage
from pages.auth_web_page import AuthWebPage
from pages.item_page import ItemPage
import time


def test_auth_web_page(driver):

    page = AuthWebPage(driver, DB.BASE_URL_AUTH)
    page.open()
    page.fill_the_field(AWPL.LOGIN_FIELD, DB.LOGIN)
    page.fill_the_field(AWPL.PASSWORD_FIELD, DB.PASSWORD)
    page.element_should_be_disable(AWPL.SUBMIT_BUTTON)
    page.click_button(AWPL.CHECK_BOX)
    page.element_should_be_enable(AWPL.SUBMIT_BUTTON)
    page.click_button(AWPL.SUBMIT_BUTTON)
    time.sleep(3)




