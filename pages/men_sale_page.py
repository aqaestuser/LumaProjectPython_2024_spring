from pages.components.nav_wigdet import NavComponent
from data.links import MEN_SALE_PAGE_URL
from selene.support.conditions import be, have
from selene.support.shared.jquery_style import s, ss
from pages.locators import BaseLocators as Header, MenSaleLocators as ms_locators
from data.page_data import MenSalePageData as data


class MenSalePage:
    def __init__(self, browser):
        self.browser = browser
        self.nav = NavComponent()

    def open_page(self):
        self.browser.open(MEN_SALE_PAGE_URL)

    @staticmethod
    def get_bread_crumbs():
        elements = ss(Header.BREADCRUMBS_LIST)
        breadcrumbs_titles = []
        for i in elements:
            breadcrumbs_titles.append(i.locate().text)
        return breadcrumbs_titles

    @staticmethod
    def are_bread_crumbs_present():
        return s(Header.BREADCRUMBS).should(be.present)

    @staticmethod
    def is_page_title_present():
        return s(ms_locators.PAGE_TITLE).should(be.present)

    @staticmethod
    def is_page_title_correct():
        return s(ms_locators.PAGE_TITLE).should(have.text(data.page_title))

    @staticmethod
    def get_number_of_items_in_te_list():
        return str(len(ss(ms_locators.LIST_ITEM)))

    def is_number_of_items_in_toolbar_corresponds_to_amount_in_list(self):
        number = self.get_number_of_items_in_te_list()
        return s(ms_locators.TOOLBAR_NUMBER).should(have.text(number))

    def are_only_product_cards_for_men_present(self):
        cards = self.get_product_cards()
        for card in cards:
            card.should(have.attribute("src").value_containing("/m/"))

    @staticmethod
    def get_product_cards():
        return ss(ms_locators.PRODUCT_IMAGE)

    @staticmethod
    def is_product_list_present():
        return s(ms_locators.PRODUCT_LIST).should(be.present)
