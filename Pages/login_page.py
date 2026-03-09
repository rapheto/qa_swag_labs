from Pages.base_page import BasePage
from Pages.menu_page import MenuPage
from selenium.webdriver.common.by import By
from logger import log

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.SWAG_LABS_URL = 'https://www.saucedemo.com/'
        self.LOGIN_USERNAME_FIELD_ID = 'user-name'
        self.LOGIN_PASSWORD_FIELD_ID = 'password'
        self.LOGIN_BUTTON_ID = 'login-button'
        
    def navigate(self):
        log.info("Open Swag Labs Website")
        return self.driver.get(self.SWAG_LABS_URL)
    
    def fill_username_field(self, username):
        log.info("Fill username")
        self.send_keys_to_element(By.ID, self.LOGIN_USERNAME_FIELD_ID, username)
        
    def fill_password_field(self, password):
        log.info("Fill password")
        self.send_keys_to_element(By.ID, self.LOGIN_PASSWORD_FIELD_ID, password)
        
    def click_login_button(self):
        log.info("Click login button")
        self.click_element(By.ID, self.LOGIN_BUTTON_ID)
        return MenuPage(self.driver)