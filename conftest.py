import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from pages.product_page import ProductPage
from pages.locators import DataBase as DB
from pages.locators import BasePageLocators as BPL


@pytest.fixture
def chrome_opt():
    options = Options()
    options.add_argument('--windows size = 100, 100')
    options.add_argument('--headless')
    options.add_argument('--incognito')
    return options

@pytest.fixture
def driver(chrome_opt):
    print('\n Start testing')
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    # try:
    #     driver.find_element(*BPL.BURGER_MENU_BUTTON).click()
    # except ElementClickInterceptedException:
    #     return True
    # driver.find_element(*BPL.BURGER_LOGOUT).click()
    # time.sleep(2)
    print('\n Finish testing')
    driver.quit()

@pytest.fixture
def authorization(driver):

    driver.get(DB.BASE_URL)
    driver.find_element(*BPL.LOGIN_FIELD).send_keys(DB.LOGIN)
    driver.find_element(*BPL.PASSWORD_FIELD).send_keys(DB.PASSWORD)
    driver.find_element(*BPL.LOGIN_KEY).click()
    yield #driver
    try:
        driver.find_element(*BPL.BURGER_MENU_BUTTON).click()
    except ElementClickInterceptedException:
        return True
    driver.find_element(*BPL.BURGER_LOGOUT).click()
    #time.sleep(2)

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout = 10)
    return wait

    


