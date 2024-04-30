from selene import by, be, have
from selene.support.shared.jquery_style import s
from data.data_checkout import CheckoutData as test_data


class CheckoutPage:

    EMAIL_FIELD = "input[id='customer-email'"
    FNAME_FIELD = "input[name='firstname']"
    LNAME_FIELD = "input[name='lastname']"
    STREET_FIELD = "input[name='street[0]']"
    CITY_FIELD = "input[name='city']"
    STATE_SELECT = "select[name='region_id']"
    STATE_OPTION = "select[name='region_id'] option[value='18']"
    POSTCODE_FIELD = "input[name='postcode']"
    COUNTRY_SELECT = "select[name='country_id']"
    COUNTRY_OPTION = "select[name='country_id'] option[value='US']"
    PHONE_FIELD = "//input[@name='telephone']"
    FLATRATE_RATIO = "//input[@value='flatrate_flatrate']"
    CONTINUE_BTN = "//button[@class='button action continue primary']"
    PLACE_ORDER_BTN = "//button[@class='action primary checkout']"
    COMPLETE_TITLE = "//span[@data-ui-id='page-title-wrapper']"
    


    _url_product = "https://magento.softwaretestingboard.com/argus-all-weather-tank.html"
    _url_cart = "https://magento.softwaretestingboard.com/checkout/cart/"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        return self.browser.open(self._url_product)

    def add_item_to_cart(self):
        self.browser.element("div[id='option-label-size-143-item-168']").click()
        self.browser.element("div[id='option-label-color-93-item-52']").click()
        self.browser.element("button[id='product-addtocart-button']").click()

    def redirect_to_checkout(self):
        self.redirect_to_cart()
        s("(//button[@class='action primary checkout'])[2]").should(be.clickable).click()
    
    def redirect_to_cart(self):
        s("div[class='message-success success message']").should(have.text("You added Argus All-Weather Tank to your shopping cart."))
        self.browser.open(self._url_cart)

    def fill_shipping_info(self):
        s(self.EMAIL_FIELD).type(test_data.EMAIL)
        s(self.FNAME_FIELD).type(test_data.FNAME)
        s(self.LNAME_FIELD).type(test_data.LNAME)
        s(self.STREET_FIELD).type(test_data.STREET)
        s(self.CITY_FIELD).type(test_data.CITY)
        self._select_option(self.STATE_SELECT, self.STATE_OPTION)
        s(self.POSTCODE_FIELD).type(test_data.POSTCODE)
        self._select_option(self.COUNTRY_SELECT, self.COUNTRY_OPTION)
        s(self.PHONE_FIELD).type(test_data.PHONE)
        s(self.FLATRATE_RATIO).click()
        s(self.CONTINUE_BTN).click()

    def place_order(self):
        s(self.PLACE_ORDER_BTN).click()

    def is_ordering_complete(self):
        expected_text = "Thank you for your purchase!"
        s(self.COMPLETE_TITLE).should(have.text(expected_text))

    def _select_option(self, select, option):
        s(select).click()
        s(option).click()