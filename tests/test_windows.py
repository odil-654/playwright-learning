def test_windows_and_button(windows_page):
    windows_page.goto("https://the-internet.herokuapp.com/windows")
    windows_page.click_button()
    with context.expect_page() as page_info:
        page.click("text=Открыть в новой вкладке")
