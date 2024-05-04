from selene import browser, be, have
from selene.support.shared.jquery_style import s


__url = "https://magento.softwaretestingboard.com/checkout/cart/"
__product_url = "https://magento.softwaretestingboard.com/dual-handle-cardio-ball.html"
__success_add_to_cart= "You added Dual Handle Cardio Ball to your shopping cart."
__multiple_addresses_text = "Create Shipping Address"
__ADD_TO_CART = "button[title='Add to Cart']"
__SUCCESS_MSG = "div[class='message-success success message']"
__MULTIPLE_ADDRESSES = "a[class='action multicheckout']"
__TITLE_MULTIPLE_ADDRESSES = "span[data-ui-id='page-title-wrapper']"


def visit(url=__url):
    browser.open(url)

def add_item_to_cart():
    visit(__product_url)
    s(__ADD_TO_CART).should(be.clickable).click()
    s(__SUCCESS_MSG).should(have.text(__success_add_to_cart))

def check_out_multiple_addresses():
    s(__MULTIPLE_ADDRESSES).should(be.clickable).click()

def is_multiple_addresses_page():
    s(__TITLE_MULTIPLE_ADDRESSES).should(have.text(__multiple_addresses_text))