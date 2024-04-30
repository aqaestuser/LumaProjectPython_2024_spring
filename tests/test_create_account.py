from pages import create_account, message


def test_create_account(first_name, last_name, user_email, password):
    print("user: ", user_email, password)
    create_account.visit()
    create_account.new_one(first_name, last_name, user_email, password)
    message.should_be("Thank you for registering")


def test_create_account_with_empty_first_name(last_name, user_email, password):
    create_account.visit()
    create_account.new_one("", last_name, user_email, password)
    create_account.first_name_error("This is a required field.")
