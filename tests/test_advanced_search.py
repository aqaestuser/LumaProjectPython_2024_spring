import allure
from pages import advanced_search


@allure.feature("Advanced Search")
@allure.title('Empty input fields')
@allure.link('https://trello.com/c/kn91s1De/')
def test_input_fields_are_empty():
    advanced_search.open()
    advanced_search.click_search_button()
    advanced_search.message_text()


@allure.feature('Advanced Search')
@allure.title('Entering an incorrect price range')
@allure.link('https://trello.com/c/X8H9lLun/')
def test_incorrect_price_range():
    advanced_search.open()
    advanced_search.fill_wrong_price_range()
    advanced_search.click_search_button()
    advanced_search.price_range_error_message()


@allure.feature('Advanced Search')
@allure.title('Entering prohibited characters in the “Price from” and “Price to” fields')
@allure.link('https://trello.com/c/HCQ997pb/')
def test_prohibited_characters_in_price():
    advanced_search.open()
    advanced_search.fill_prohibited_characters_in_price()
    advanced_search.click_search_button()
    advanced_search.invalid_number_price_error_message()


@allure.feature('Advanced Search')
@allure.title('Products found match the search criteria')
@allure.link('https://trello.com/c/fpWChrDR/')
def test_correct_results_of_the_advanced_search():
    advanced_search.open()
    advanced_search.search_by_product_name()
    advanced_search.click_search_button()
    advanced_search.check_search_result()


@allure.feature('Advanced Search')
@allure.title('Filling out all input fields')
@allure.link('https://trello.com/c/Pz12v6Hs/')
def test_all_input_fields_are_filled_in():
    advanced_search.open()
    advanced_search.fill_in_all_input_fields('Jacket', 'MJ03', 'Adjustable hood.', 'Adjustable hood.', '40', '50')
    advanced_search.click_search_button()
    advanced_search.check_full_search_results('Jacket', 'MJ03', 'Adjustable hood.', 40, 50)


@allure.feature('Advanced Search')
@allure.title('Search for a non-existent product')
@allure.link('https://trello.com/c/cfPCcQjS/')
def test_non_existent_product():
    advanced_search.open()
    advanced_search.fill_non_existent_product_name()
    advanced_search.click_search_button()
    advanced_search.check_search_results_for_non_existent_product()
