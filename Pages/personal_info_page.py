from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from logger import log

class PersonalInfoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        #PI = PERSONAL INFORMATION
        self.PI_CONTINUE_BUTTON_ID = 'continue'
        self.PI_ERROR_MESSAGE_CLASS = 'error-message-container'
    
    def click_continue_button(self):
        log.info("Click continue button")
        self.click_element(By.ID, self.PI_CONTINUE_BUTTON_ID)
        
    def get_error_message(self):
        log.info("Get error message")
        return self.get_element_text(By.CLASS_NAME, self.PI_ERROR_MESSAGE_CLASS)
    
    def verify_that_error_is_shown(self):
        log.info("Verifying error message")
        return self.get_error_message() == "Error: First Name is required"