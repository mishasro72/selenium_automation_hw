from selenium.webdriver.common.by import By


# BASE_URL = 'https://www.saucedemo.com/'

class BasePageLocators():
    LOGIN_FIELD = (By.XPATH, '//*[@id="user-name"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN_KEY = (By.XPATH, '//*[@id="login-button"]')
    LOGIN_ERROR_MES = (By.XPATH, '//form/div/h3')
    BASKET_ICON = (By.XPATH, "//a[@class = 'shopping_cart_link']")
    SHOPING_CART_BADGE = (By.XPATH, "//span[@class = 'shopping_cart_badge']")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    BURGER_LOGOUT = (By.XPATH, "//a[@id='logout_sidebar_link']")
    BURGER_ABOUT = (By.XPATH, "//a[@id='about_sidebar_link']")
    BURGER_REST_APP = (By.XPATH, "//a[@id='reset_sidebar_link']")
    CLOSE_BURGER_MENU = (By. XPATH, "//button[@id='react-burger-cross-btn']")


    # REMOVE_FIRST_ITEM_FROM_CATALOG_BUT = (By.XPATH, "//button[@id = 'remove-sauce-labs-backpack']")
    # ADD_TO_CART_BUT= (By.XPATH, "//button[@id = 'add-to-cart']")

# class MainPageLocators():

#     CART_ICON = (By.XPATH, "//a[@class = 'shopping_cart_link']")

class ItemPageLocators():
    ADD_TO_CART_BUT = (By.XPATH, "//button[@id = 'add-to-cart']")
    REMOVE_ITEM_BUT= (By.XPATH, "//button[@id = 'remove']")


#locators
#authorization
LOGIN_FIELD = (By.XPATH, '//*[@id="user-name"]')
PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
LOGIN_KEY = (By.XPATH, '//*[@id="login-button"]')
LOGIN_ERROR_MES = (By.XPATH, '//form/div/h3')

#cart
class ProductPageLocators():
    FIRST_ITEM = (By.XPATH, "//*[@id='item_4_title_link']/div")
    FIRST_ITEM_PRICE = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    ADD_TO_BASKET_FIRST_BUT = (By.XPATH, "//button[@id= 'add-to-cart-sauce-labs-backpack']")
    ADD_TO_CART_SECOND_BUT = (By.XPATH, "//button[@id = 'add-to-cart-sauce-labs-bike-light']")
    IMAGE_OF_FIRST_ITEM = (By.XPATH, "//img[@alt = 'Sauce Labs Backpack']")
    SORT_BUTTON = (By.XPATH, "//select[@class='product_sort_container']")
    LIST_OF_ITEMS = (By.XPATH, "//div[@class='inventory_item_name ']")
    LIST_OF_PRICES = (By.XPATH, "//div[@class='inventory_item_price']")

    # SHOPING_CART_BADGE = (By.XPATH, "//span[@class = 'shopping_cart_badge']")
    # BASKET_ICON = (By.XPATH, "//a[@class = 'shopping_cart_link']")
    # REMOVE_FIRST_ITEM_FROM_CATALOG_BUT = (By.XPATH, "//button[@id = 'remove-sauce-labs-backpack']")

class BasketPageLocators():
    FIRST_ITEM_NAME = (By.XPATH, "//*[@id='item_4_title_link']/div")
    FIRST_ITEM_PRICE = (By.XPATH, "//div[@class = 'inventory_item_price']")
    REMOVE_FIRST_ITEM_FROM_CATALOG_BUT = (By.XPATH, "//button[@id = 'remove-sauce-labs-backpack']") 
    CHECKOUT_BUTTON = (By.XPATH, "//button[@id = 'checkout']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id = 'continue']")
    FINISH_BUTTON = (By.XPATH, "//button[@id = 'finish']")
    CHECKOUT_FORM_FNAME = (By.XPATH, "//input[@id = 'first-name']")
    CHECKOUT_FORM_LNAME = (By.XPATH, "//input[@id = 'last-name']")
    CHECKOUT_FORM_ZIP = (By.XPATH, "//input[@id = 'postal-code']")
    COMPLETE_MESSAGE = (By.XPATH, "//h2[@class='complete-header']")

class AuthWebPageLocators():

    LOGIN_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    CHECK_BOX = (By.ID, 'agreement')
    SUBMIT_BUTTON = (By.ID, 'registerButton')

class WaitPageLocators():

    TITLE_H1 = (By.XPATH, "//h1")
    LOAD_START_BUTTON = (By.XPATH, "//*[@id='startTest']")
    LOADER_SIGN = (By.XPATH, "//*[@id='loader']")
    LOGIN_FIELD = (By.XPATH, "//*[@id='login']")
    PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")
    AGREE_FIELD = (By.XPATH, "//*[@id='agree']")
    REGISTER_BUTTON = (By.XPATH, "//*[@id='register']")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='successMessage']")
    FIRST_BROKEN_IMG = (By.XPATH, "//img[@src = 'asdf.jpg']")
    ALL_IMG = (By.XPATH, "//img")
    NON_BROKEN_IMG = (By.XPATH, "//img[@src = '/img/forkme_right_green_007200.png']")                
    SUCCESS_MESSAGE_BASIC_AUTH = (By.CSS_SELECTOR, "div>p")
    



class DataBase():
    LOGIN = 'standard_user'
    PASSWORD = 'secret_sauce'

    LOGIN_NEGATIVE = 'login'
    PASSWORD_NEGATIVE = 'password'
    BASE_URL = 'https://www.saucedemo.com/'
    BASE_URL_AUTH = "https://victoretc.github.io/webelements_information/"
    BASE_URL_WAIT = "https://victoretc.github.io/selenium_waits/"
    BASE_URL_BROKEN_IMG = "https://the-internet.herokuapp.com/broken_images"
    BASE_URL_BASE_AUTH = "https://the-internet.herokuapp.com/basic_auth"


