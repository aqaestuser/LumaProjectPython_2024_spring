import allure
from selene import browser
from selene.support.conditions import have
from selene.support.shared.jquery_style import s
from pages.whats_new_page import WhatsNewPage
from pages.locators import ProductItemLocators as Product
from pages.locators import LoginPageLocators as Login


@allure.link('https://trello.com/c/jgLmzBZX')
@allure.suite("US_006.004 | What's new > Eco Collection New")
@allure.feature("TC_006.004.005 | What's new > Eco Collection New")
def test_add_product_to_wishlist_as_non_logged_in_user():
    message = "You must login or register to add items to your wishlist"
    page = WhatsNewPage(browser=browser)
    with allure.step("Assert current url == What's New Page url"):
        page.open_page()
        page.is_current_link()
    with allure.step("Click button new yoga"):
        page.is_button_visible()
        page.click_button_shop_new_yoga()
    with allure.step("Go to product item"):
        product = s(Product.ITEM_INFO)
        page.scroll_to(product)
        product.hover()
    with allure.step("Add to Wish List"):
        s(Product.WISH_LIST).click()
    with allure.step("Redirect to Customer Login and verify message"):
        s(Login.PAGE_TITLE_WRAPPER).should(have.text("Customer Login"))
        s(Login.MESSAGE_TEXT).should(have.text(message))
