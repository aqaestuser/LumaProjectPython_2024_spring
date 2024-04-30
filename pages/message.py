from selene import browser, by, be, have
from selene.support.shared.jquery_style import s, ss

MESSAGE = "div.messages [data-bind ^='html']"


def should_be(partial_text):
    s(MESSAGE).should(have.text(partial_text))
