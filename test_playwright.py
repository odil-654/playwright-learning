from playwright.sync_api import expect
from faker import Faker

fake = Faker()
BASE_URL = "http://144.31.63.127:5000/"


def test_invalid_login(page):
    username = fake.user_name()
    password = fake.password()

    page.goto(BASE_URL)
    page.get_by_test_id("nav-login").click()
    page.get_by_test_id("login-username").fill(username)
    page.get_by_test_id("login-password").fill(password)
    page.get_by_test_id("login-submit").click()
    loader = page.get_by_test_id("login-submit-spinner")
    expect(loader).to_be_visible()
    expect(loader).not_to_be_visible()
    error_message = page.get_by_test_id("login-error-inline")

    expected_error = "Invalid login or password."
    actual_error = error_message.text_content()

    assert actual_error == expected_error, (
        f"Expected: '{expected_error}', "
        f"Actual: '{actual_error}'"
    )