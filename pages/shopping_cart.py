from selene import browser, be, have
from selene.support.shared.jquery_style import s


url = "https://magento.softwaretestingboard.com/checkout/cart/"
product_url = "https://magento.softwaretestingboard.com/dual-handle-cardio-ball.html"
success_add_to_cart= "You added Dual Handle Cardio Ball to your shopping cart."
multiple_addresses_text = "Create Shipping Address"
ADD_TO_CART = "button[title='Add to Cart']"
SUCCESS_MSG = "div[class='message-success success message']"
MULTIPLE_ADDRESSES = "a[class='action multicheckout']"
TITLE_MULTIPLE_ADDRESSES = "span[data-ui-id='page-title-wrapper']"


def visit(url=url):
    browser.open(url)

def add_item_to_cart():
    visit(product_url)
    s(ADD_TO_CART).should(be.clickable).click()
    s(SUCCESS_MSG).should(have.text(success_add_to_cart))

def check_out_multiple_addresses():
    s(MULTIPLE_ADDRESSES).should(be.clickable).click()

def is_multiple_addresses_page():
    s(TITLE_MULTIPLE_ADDRESSES).should(have.text(multiple_addresses_text))
