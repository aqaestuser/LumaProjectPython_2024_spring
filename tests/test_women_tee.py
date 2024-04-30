from pages.locators import SalePageLocators, BaseLocators
from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss
import allure


@allure.link('https://trello.com/c/fhLdyS1l')
def test_011_016_001_women_tees_breadcrumbs_is_correct():
    browser.open(SalePageLocators.LINK_TEES_WOMEN)
    ss(BaseLocators.BREADCRUMBS_LIST).should(have.texts('Home', 'Women', 'Tops', 'Tees'))

