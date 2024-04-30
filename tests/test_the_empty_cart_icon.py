from pages import empty_cart_icon_page


def test_the_cart_icon():
    empty_cart_icon_page.open_main_page()
    empty_cart_icon_page.check_the_cart_icon_is_visible()
    empty_cart_icon_page.check_the_cart_icon_is_clickable()
    empty_cart_icon_page.check_open_new_window_after_click_on_the_cart_icon()
