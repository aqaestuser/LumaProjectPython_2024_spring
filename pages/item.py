from selene import be
from selene.support.shared.jquery_style import s


ADD_TO_CART = "button[id='product-addtocart-button']"
SIZE_M = "(//div[@index='2'])[1]"
SIZE_S = "(//div[@index='1'])[1]"
SIZE_XS = "(//div[@index='0'])[1]"
BLACK_COLOR = "(//div[@index='0'])[2]"
SUCCESS_MSG = "div[data-ui-id='message-success']"


class Item:
    
    def __init__(self, browser, url):
        self._url = url
        self._browser = browser

    def visit(self):
        self._browser.open(self._url)
    
    def choose_size(self, size):
        if size == 'M':
            s(SIZE_M).should(be.clickable).click()
        if size == 'S':
            s(SIZE_S).should(be.clickable).click()
        if size == 'XS':
            s(SIZE_XS).should(be.clickable).click()
    
    def choose_color(self):
        s(BLACK_COLOR).should(be.clickable).click()

    def add_to_cart(self):
        s(ADD_TO_CART).should(be.clickable).click()
    
    def is_success_message_appears(self):
        s(SUCCESS_MSG).should(be.visible)    
    