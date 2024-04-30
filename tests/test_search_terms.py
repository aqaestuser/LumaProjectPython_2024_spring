from pages.locators import SearchTermsLocators as ST
from pages.locators import BaseLocators as Base
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
import allure


@allure.link('https://trello.com/c/tnpU7rqU')
def test_015_001_001_search_terms_title_is_visible():
    browser.open(ST.LINK_SEARCH_TERMS)
    s(Base.PAGE_TITLE).should(have.text("Popular Search Terms"))


@allure.link('https://trello.com/c/9oDGaMAB')
def test_015_001_002_count_search_terms():
    browser.open(ST.LINK_SEARCH_TERMS)
    ss(ST.TERMS_FOR_SEARCH_LIST_QTY).should(have.size(100))

