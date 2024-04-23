from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from .locators import WaitPageLocators as WPL
from .base_page import BasePage
from .data import AssertationPhrases as AP
from .data import DataForBaseAuth as DFBA
#from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.remote.webelement import WebElement
from faker import Faker


class WaitPageClass(BasePage):
    def click_on_wait_element(self):
        self.wait_for_element_clickable(WPL.LOAD_START_BUTTON)

    def click_on_agree(self):
        self.click_button(WPL.AGREE_FIELD)

    def click_on_registration_button(self):
        self.click_button(WPL.REGISTER_BUTTON)

    def check_the_wait_page_title(self):
        assert self.get_text(WPL.TITLE_H1) == AP.H1_wait_page, "ОШИБКА!"

    def check_the_loader_sign(self):
        assert self.is_element_visible(WPL.LOADER_SIGN), "ОШИБКА! Элемент невидим"

    def check_the_success_message(self):
        #print(self.get_text(WPL.SUCCESS_MESSAGE))
        self.is_element_visible(WPL.SUCCESS_MESSAGE)
        assert self.get_text(WPL.SUCCESS_MESSAGE) == AP.SUCCESS_REGISTRAITION_MESSAGE, "ОШИБКА!"

    def check_success_basic_auth(self):
        self.is_element_visible(WPL.SUCCESS_MESSAGE_BASIC_AUTH)
        assert self.get_text(WPL.SUCCESS_MESSAGE_BASIC_AUTH) == AP.BASIC_AUTH_SUCCESS

    def check_for_broken_image(self):
        self.find_broken_img(WPL.ALL_IMG)

    def fill_the_login_field(self):
        fake = Faker()
        self.fill_the_field(WPL.LOGIN_FIELD, fake.name())

    def fill_the_password_field(self):
        fake = Faker()
        self.fill_the_field(WPL.PASSWORD_FIELD, fake.password())

    def popup_auth_wait(self):
        self.popup_auth_base(DFBA.POPUP_USERNAME, DFBA.POPUP_PASSWORD)

    #def check_all_images_displayed(self):




    
