from selene import browser, be, have
from selene.support.shared.jquery_style import s, ss

url = "https://magento.softwaretestingboard.com/customer/account/login"


def visit():
    browser.open(url)


def login(user, password):
    s("div.login-container #email").type(user)
    s("div.login-container #pass").type(password)
    s("div.login-container #send2").click()
