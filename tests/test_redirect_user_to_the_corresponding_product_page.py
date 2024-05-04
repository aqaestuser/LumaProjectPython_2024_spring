import time

import allure
from selene import browser
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.action_chains import ActionChains

url = "https://magento.softwaretestingboard.com/"
@allure.link('https://trello.com/c/n0EPl2TJ/257')
def test_redirect_user_to_the_corresponding_product_page():
    browser.open(url)
    product_cards = ss('[class="product-item-info"]').second.click()

    s('[class="product data items"]').should(have.text('Details'))

    time.sleep(5)

