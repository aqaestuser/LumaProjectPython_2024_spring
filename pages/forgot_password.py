from selene import browser
from selene.support.shared.jquery_style import s

url = "https://magento.softwaretestingboard.com/customer/account/forgotpassword/"


def visit():
    browser.open(url)


def reset(user_email):
    s("#email_address").type(user_email).press_enter()
