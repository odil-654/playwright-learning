from playwright.sync_api import sync_playwright, expect


def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://144.31.63.127:5000/")
        page.get_by_test_id("nav-login").click()
        page.get_by_test_id("login-username").fill("test123")
        page.get_by_test_id("login-password").fill("test12345")
        page.get_by_test_id("login-submit").click()
        loader = page.get_by_test_id("login-submit-spinner")
        expect(loader).to_be_visible()
        expect(loader).not_to_be_visible()
        error_message = page.get_by_test_id("login-error-inline")


        browser.close()
