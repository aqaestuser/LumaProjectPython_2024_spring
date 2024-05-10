import allure
from pages import performans_new_page
from selenium.webdriver.common.by import By
from pages.locators import PerformanceSportswear, BaseLocators, LoginLocators, ProductLocators
from data.links import *
from selene import browser, be, have, query, command
from selene.support.shared.jquery_style import s, ss
from selene.support.conditions import be, have


@allure.feature(" What's new > Performance Sportswear New > Check count of products")
@allure.link("https://trello.com/c/REIhcQnq")
def test_check_count_of_products(login):
    performans_new_page.visit()
    assert performans_new_page.items_count() == 5


@allure.link("https://trello.com/c/9B5bXFEP")
def test_006_008_001_visibility_of_price_photo_name():
    # I can't count elements on the page via selen
    browser.open(PerformanceSportswear.LINK_SPORT)
    ss(BaseLocators.PRODUCT_NAME).should(have.size(5))
    ss(BaseLocators.PRODUCT_PRICE).should(have.size(5))
    ss(BaseLocators.PRODUCT_IMAGE).should(have.size(5))


@allure.link("https://trello.com/c/cmwZ3A6P")
def test_006_008_002_add_to_cart_from_catalog_without_color_and_size():
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    # кликнуть невидимую кнопку - она за пределами экрана и/или не отрисована
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).perform(command.js.click)
    s(PerformanceSportswear.SUCCESS_MESSAGE).should(have.no.text(PerformanceSportswear.TEXT_SUCCESS_MESSAGE))


@allure.link("https://trello.com/c/cmwZ3A6P")
def test_006_008_002_add_to_cart_from_catalog_without_color_and_size_with_hover():
    # other variant
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    s(PerformanceSportswear.IMAGE_2).should(be.visible).hover()
    s(PerformanceSportswear.BUTTON_ADD_ITEM2).should(be.clickable).click()
    s(PerformanceSportswear.SUCCESS_MESSAGE).should(have.no.text(PerformanceSportswear.TEXT_SUCCESS_MESSAGE))


@allure.link("https://trello.com/c/WjUokO7r")
def test_006_008_003_color_and_size_can_be_checked():
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    s(PerformanceSportswear.IMAGE_2).click()
    s(ProductLocators.SIZE_XS).click()
    s(ProductLocators.COLOR_BLUE).click()
    selected = ss('[aria-checked="true"]')
    assert len(selected) == 2


@allure.link("https://trello.com/c/dYQgmbfJ")
def test_006_008_004_add_to_cart_from_product_page_without_color_and_size():
    browser.open(LINK_LOGIN)
    s(LoginLocators.FIELD_NAME).type("ahahah1@gmail.com")
    s(LoginLocators.FIELD_PASSWORD).type("jk$34_tor")
    s(LoginLocators.BUTTON_SUBMIT).click()
    browser.open(LINK_SPORT)
    s(PerformanceSportswear.IMAGE_2).click()
    s(ProductLocators.ADD_TO_CART_BUTTON).click()
    chooses = ss(ProductLocators.SHOULD_CHOOSE_SIZE_AND_COLOR)
    for choose in chooses:
        assert choose.text == ProductLocators.TEXT_REQUIRED_FIELD
