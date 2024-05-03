import allure
import data.links as links
from pages.shopping_cart_page import ShoppingCartPage
from selene import browser


class TestShoppingCart:

    @allure.link("https://trello.com/c/nBYV0Aum/208-tc005001006-main-page-cart-proceed-to-checkout-via-shopping-cart")
    @allure.feature("Main page > Cart > View and edit cart")
    @allure.title("TC_005.001.006 | Main page > Cart > Proceed to Checkout via shopping cart")
    def test_procceed_checkout_from_shopping_cart(self):
        page = ShoppingCartPage(browser, links.SHOPPING_CART)
        page.adding_item()
        with allure.step("Navigate to the shopping cart page"):
            page.visit()
        with allure.step("Click on the “Proceed to Checkout“ button"):
            page.proceed_to_checkout()
        page.is_shipping_page()
        