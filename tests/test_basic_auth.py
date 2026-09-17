from core.base_url import Urls


def test_basic_authorization(basic_auth_page):
    login = "admin"
    password = "admin"
    basic_auth_page.actions.goto(Urls.get_basic_auth_url(login, password))
    text_1 = basic_auth_page.get_success_message()
    text_2 = "Congratulations! You must have the proper credentials."
    assert text_1 == text_2, (
        f"Expected: '{text_2}', "
        f"Actual: '{text_1}'"
    )
