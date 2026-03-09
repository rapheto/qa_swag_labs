from Pages.login_page import LoginPage

def test_remove_items_from_cart_ts_003(driver):
    login_page = LoginPage(driver)
    
    #Login
    login_page.navigate()
    login_page.fill_username_field("problem_user")
    login_page.fill_password_field("secret_sauce")
    menu_page = login_page.click_login_button()
    
    menu_page.add_item_to_cart()
    cart_page = menu_page.go_to_cart()
    
    assert cart_page.verify_that_are_items_on_cart("Sauce Labs Backpack")
    cart_page.remove_item_from_cart()
    assert not cart_page.verify_that_backpack_is_not_displayed()