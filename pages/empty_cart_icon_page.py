import allure
from selene import browser, by, be, have, support
from selene.support.shared.jquery_style import s

base_url = "https://magento.softwaretestingboard.com/"


def open_main_page():
    browser.open(base_url)


def check_the_cart_icon_is_visible():
    browser.open(base_url)
    s(by.css("a[class='action showcart']")).should(be.visible)
    s(by.css("a[class='action showcart']")).click()
    s(by.css("strong[class='subtitle empty']")).should(be.visible)
    s(by.css("strong[class='subtitle empty']")).should(have.text("You have no items in your shopping cart."))


def check_the_cart_icon_is_clickable():
    browser.open(base_url)
    s(by.css("a[class='action showcart']")).should(be.clickable)


def check_open_new_window_after_click_on_the_cart_icon():
    browser.open(base_url)
    s(by.css("a[class='action showcart']")).click()
    s(by.css("strong[class='subtitle empty']")).should(be.visible)
    s(by.css("strong[class='subtitle empty']")).should(have.text("You have no items in your shopping cart."))
