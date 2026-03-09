from Pages.base_page import BasePage
from Pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from logger import log

class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #Locators
        self.MENU_ADD_TO_CART_BUTTON_SAUCE_LABS_BACKPACK_ID = 'add-to-cart-sauce-labs-backpack'
        self.CART_ICON_ID = 'shopping_cart_container'
        
    def add_item_to_cart(self):
        log.info("Add item to cart")
        self.click_element(By.ID, self.MENU_ADD_TO_CART_BUTTON_SAUCE_LABS_BACKPACK_ID)
        
    def go_to_cart(self):
        log.info("Go to cart")
        self.click_element(By.ID, self.CART_ICON_ID)
        return CartPage(self.driver)
    
    