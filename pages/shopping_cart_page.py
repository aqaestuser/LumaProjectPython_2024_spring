import data.links as links
from selene import be, have
from selene.support.shared.jquery_style import s
from data.page_data import ShippingData as data
from pages.item import Item

PROCEED_TO_CHECKOUT = "button[data-role='proceed-to-checkout']"
SHIPPING_TITLE = "(//div[@class='step-title'])[1]"

class ShoppingCartPage:

    def __init__(self, browser, url):
        self._browser = browser
        self._url = url

    def visit(self):
        self._browser.open(self._url)
    
    def proceed_to_checkout(self):
        s(PROCEED_TO_CHECKOUT).should(be.clickable).click()

    def is_shipping_page(self):
        s(SHIPPING_TITLE).should(have.exact_text(data.shipping_address))
    
    def adding_item(self):
        item = Item(self._browser, links.HERO_HOODIE)
        item.visit()
        item.choose_size('M')
        item.choose_color()
        item.add_to_cart()
        item.is_success_message_appears()
    
