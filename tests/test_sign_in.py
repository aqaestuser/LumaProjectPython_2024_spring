import allure

from pages import sign_in, my_account, message


@allure.link("https://trello.com/c/V3vp6nIt")
@allure.feature("Sign in & Registration, Account >Sign in_(authorization)")
def test_sign_in_with_good_credentials():
    sign_in.visit()
    sign_in.login("pamela341714226113@example.com", "@8j%Yltt(E")
    my_account.page_title("My Account")

