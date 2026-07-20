from core.base_url import Urls


def test_number_of_scrolls(scroll_page):
    scroll_page.actions.goto(Urls.SCROLL)
    max_attempts = 500
    attempts = 0
    while True:
        items = scroll_page.get_number_of_scrolls()
        if len(items) >= 10:
            break
        if attempts >= max_attempts:
            raise Exception("Too many attempts")
        scroll_page.get_scroll_a_bit()
        attempts += 1