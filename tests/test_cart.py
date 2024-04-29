from selene import browser, by, be, have


class TestCart:

    def test_proceed_to_checkout_with_valid_data(self):
        browser.open("https://magento.softwaretestingboard.com/checkout/cart/")
        browser.element(by.css("span[data-ui-id='page-title-wrapper']")).should(have.text('Shopping Cart'))
        