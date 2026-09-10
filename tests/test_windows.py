from core.base_url import Urls
from pages.new_window_page import NewWindowPage


def test_windows_and_button(windows_page):
    windows_page.actions.goto(Urls.WINDOWS)

    new_page_1 = windows_page.click_and_get_new_page()
    actual_1 = NewWindowPage(new_page_1).get_text_in_page()
    assert actual_1 == "New Window", f"Expected: 'New Window', Actual: '{actual_1}'"

    windows_page.actions.bring_to_front()

    new_page_2 = windows_page.click_and_get_new_page()
    actual_2 = NewWindowPage(new_page_2).get_text_in_page()
    assert actual_2 == "New Window", f"Expected: 'New Window', Actual: '{actual_2}'"

    windows_page.actions.bring_to_front()
    new_page_1.close()
    new_page_2.close()

    actual_pages = len(windows_page.page.context.pages)
    assert actual_pages == 1, f"Expected: 1, Actual: '{actual_pages}'"