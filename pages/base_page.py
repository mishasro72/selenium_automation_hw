from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .locators import DataBase as DB
from .locators import BasePageLocators as BPL
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement
import requests

class BasePage():

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self) -> WebElement:
        self.driver.get(self.url)

    def click_button(self, locator: tuple) -> WebElement:
        self.driver.find_element(*locator).click()

    def choose_element(self, locator: tuple):
        return self.driver.find_element(*locator)
    
    def choose_elements(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def check_the_basket_not_empty(self):
        assert self.get_text(BPL.SHOPING_CART_BADGE) == '1'

    def basket_is_empty(self):
        assert self.is_element_not_present(BPL.SHOPING_CART_BADGE), "Basket is not empty"

    def get_text(self, locator: tuple) -> str:
        return self.driver.find_element(*locator).text
    
    def get_items_names(self, locator: tuple):
        items = self.choose_elements(locator)
        names = []
        for item in items:
            names.append(item.text)
        return names

    def get_items_prices(self, locator: tuple):
        items = self.choose_elements(locator)
        prices = []
        for item in items:
            price = item.text.replace('$', '')
            prices.append(float(price))
        return prices
    
    def go_to_basket(self) -> WebElement:
        self.click_button(BPL.BASKET_ICON)

    def fill_the_field(self, locator: tuple, text: str):
        self.driver.find_element(*locator).send_keys(text)

    def should_be_first_item_page(self):
        assert self.driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4", "It's not the first item page"

    def should_be_base_url_page(self):
        assert self.driver.current_url == DB.BASE_URL, "It's not base url page"

    def should_be_basket_page(self):
        assert self.driver.current_url == "https://www.saucedemo.com/cart.html", "It's not a basket page"

    def should_be_about_page(self):
        assert self.driver.current_url == "https://saucelabs.com/", "It's not about url page"

    def burger_menu_logout(self):
        self.click_button(BPL.BURGER_MENU_BUTTON)
        self.click_button(BPL.BURGER_LOGOUT)
    
    def burger_menu_about(self):
        self.click_button(BPL.BURGER_MENU_BUTTON)
        self.click_button(BPL.BURGER_ABOUT)

    def burger_menu_rest_app(self):
        self.click_button(BPL.BURGER_MENU_BUTTON)
        self.click_button(BPL.BURGER_REST_APP)
        #self.click_button(BPL.CLOSE_BURGER_MENU)


    def check_element_is_displayed(self, locator: tuple):
        assert self.is_element_displayed(locator), "ОШИБКА! Изображение не показывается"

    def check_all_elements_displayed(self, locator: tuple):
        elements = self.driver.find_elements(*locator)
        i = 0
        if len(elements) != 0:
            for i, element in enumerate(elements):
                if not element.is_displayed():
                    print(f"Element with index {i} isn't displayed")
    
    def find_broken_img(self, locator: tuple):
        images = self.driver.find_elements(*locator)
        if len(images) != 0:
            for index, image in enumerate(images):
                image_source = image.get_attribute("src")
                response = requests.get(image_source)
                try:
                    assert response.status_code == 200
                except:
                    print(f'ERROR! Broken image namber {index} was found on {image_source}')     

    def switch_to_alert(self):
        self.driver.switch_to.alert

    def popup_auth_base(self, username: str, password: str) -> WebElement:
        self.driver.get(f"https://{username}:{password}@{self.url.replace('https://', '')}")
       # print(f"https://{username}:{password}@{self.url.replace('https://', '')}")
    
    def is_element_present(self, locator: tuple) -> bool:
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
    
    def is_element_not_present(self, locator: tuple, timeout = 1) -> bool:
        try:
            wait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return True
        return False  
    
    def is_element_disabled(self, locator: tuple) -> bool:
        element = self.driver.find_element(*locator)
       # print(element.is_enabled()) 
        if element.is_enabled():
            return False
        return True
    
    def is_element_displayed(self, locator: tuple):
        element = self.driver.find_element(*locator)
        return element.is_displayed()
    
    def is_element_visible(self, locator: tuple, timeout = 5):
        try:
            wait(self.driver, timeout).until(EC.visibility_of_element_located((locator)))
            return True
        except TimeoutException:
            print("ОШИБКА! Элемент не стал видимым")
        # return True
    
    def wait_for_element_clickable(self, locator: tuple):
        wait(self.driver, timeout=10).until(EC.element_to_be_clickable((locator))).click()
    
    @property
    def current_url(self) -> str:
        return self.driver.current_url
    
    
