from pages.checkout_page import CheckoutPage
from selene import browser, have


class TestCheckout:

    def test_proceed_to_checkout_with_valid_data(self):
        page = CheckoutPage(browser)
        page.open()
        page.add_item_to_cart()
        page.redirect_to_checkout()
        page.fill_shipping_info()
        page.place_order()
        page.is_ordering_complete()




