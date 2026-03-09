from Pages.login_page import LoginPage

def test_going_to_checkout_without_required_informations_ts_008(driver):
    login_page = LoginPage(driver)
    
    #Login
    login_page.navigate()
    login_page.fill_username_field("problem_user")
    login_page.fill_password_field("secret_sauce")
    menu_page = login_page.click_login_button()
    
    menu_page.add_item_to_cart()
    cart_page = menu_page.go_to_cart()
    
    assert cart_page.verify_that_are_items_on_cart("Sauce Labs Backpack")
    personal_info_page = cart_page.go_to_personal_info()
    
    personal_info_page.click_continue_button()
    assert personal_info_page.verify_that_error_is_shown()