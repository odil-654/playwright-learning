def test_basic_authorization(basic_auth_page):
    login = "admin"
    password = "admin"
    basic_auth_page.goto(f"https://{login}:{password}@the-internet.herokuapp.com/basic_auth")
    text_1 = basic_auth_page.get_success_message()
    text_2 = "Congratulations! You must have the proper credentials."
    assert text_1 == text_2
