import allure
from selene import browser
from pages import cart
from pages import erin_recommends_page
from pages.main_page import MainPage


@allure.feature("Sale > 20% OFF:")
@allure.link('https://trello.com/c/9c2BadPx')
@allure.title("Purchase of goods with a 20% discount")
def test_sale_off_purchase_of_goods_with_discount():
    with allure.step("Open main page and check if load successfully"):
        page = MainPage(browser=browser)
        page.open_page()
        page.is_loaded()
        page.scroll_to_hot_sellers()
    with (allure.step("Add to products item to card until sub total > 200")):
        products = page.products
        size = len(products)
        if size == 0:
            page = erin_recommends_page
            page.open_page()
            size = len(page.products)
        count = 0
        for i in range(0, size):
            page.add_product_to_cart(products[i])
            count += 1
            page.verify_counter(str(count))
            if page.get_subtotal() > 200:
                break
    with (allure.step("Go to checkout card with products item")):
        cart.open_page()
