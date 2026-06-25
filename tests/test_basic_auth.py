from pages.basic_auth_page import BasicAuthPage


def test_basic_authorization(page):
    basic_auth_page = BasicAuthPage(page)
    basic_auth_page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    text_1 = basic_auth_page.get_success_message()
    text_2 = "Congratulations! You must have the proper credentials."
    assert text_1 == text_2