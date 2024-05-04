import allure
import pages.shopping_cart as cart


@allure.link("https://trello.com/c/e5Gv4XR4")
@allure.feature("Main page > Cart > View and edit cart")
@allure.title("TC_005.001.007 | Main page > Cart > Proceed to Checkout with multiple addresses")
def test_proceed_to_checkout_with_multiple_addresses(login):
    cart.add_item_to_cart()
    with allure.step("Navigate to the shopping cart page"):
        cart.visit()
    with allure.step("Click on the “Check Out with Multiple Addresses“ label"):
        cart.check_out_multiple_addresses()
    cart.is_multiple_addresses_page()