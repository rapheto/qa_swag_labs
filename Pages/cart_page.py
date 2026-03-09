from Pages.base_page import BasePage

from selenium.webdriver.common.by import By
from logger import log

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.CART_REMOVE_BUTTON_SAUCE_LABS_BACKPACK_ID = 'remove-sauce-labs-backpack'
        self.CART_ITEM_CARD_SAUCE_LABS_BACKPACK_CLASS = 'inventory_item_name'
        
    def get_item_on_cart(self):
        log.info("Get item's name in the cart")
        return self.get_element_text(By.CLASS_NAME, self.CART_ITEM_CARD_SAUCE_LABS_BACKPACK_CLASS)
        
    def remove_item_from_cart(self):
        log.info("Remove item from cart")
        self.click_element(By.ID, self.CART_REMOVE_BUTTON_SAUCE_LABS_BACKPACK_ID)
    
    def verify_that_backpack_is_not_displayed(self):
        log.info("Cart is empty")
        return self.is_element_displayed(By.ID, self.CART_ITEM_CARD_SAUCE_LABS_BACKPACK_CLASS)
    
    def verify_that_are_items_on_cart(self, name):
        log.info("Verifying that are items in the cart")
        return self.get_item_on_cart() == name