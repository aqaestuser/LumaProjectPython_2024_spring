import data.links as links
from selene import browser
from pages.shopping_cart_page import ShoppingCartPage


class TestShoppingCart:

    def test_procceed_checkout_from_shopping_cart(self):
        page = ShoppingCartPage(browser, links.SHOPPING_CART)
        page.adding_item()
        page.visit()
        page.proceed_to_checkout()
        page.is_shipping_page()
        