from selene.support.shared import browser
from selene import be, have
from selene.support.shared.jquery_style import s

# Определяем объект страницы для страницы политики конфиденциальности
class PrivacyPolicyPage:
    def __init__(self):
        self.contact_us_link = s('#maincontent > div.columns > div > div.privacy-policy.cms-content > div.privacy-policy-content > p:nth-child(51) > a')

    def open(self):
        browser.open('https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode')
        return self

    def click_contact_us(self):
        self.contact_us_link.click()
        return ContactUsPage()  # Переход к объекту страницы обратной связи

# Определяем объект страницы обратной связи
class ContactUsPage:
    def __init__(self):
        self.header = s('h1')

    def should_have_correct_header(self):
        self.header.should(have.text('Whoops, our bad...'))

# Функция, реализующая тест-кейс
def test_contact_us_link_redirects_to_contact_us_page():
    # Инициализация объекта страницы политики конфиденциальности
    privacy_policy_page = PrivacyPolicyPage()
    # 1. Открыть страницу политики конфиденциальности и кликнуть по ссылке "Связаться с нами"
    contact_us_page = privacy_policy_page.open().click_contact_us()
    # Проверить, что мы находимся на странице "Обратная связь"
    contact_us_page.should_have_correct_header()