from core.base_url import Urls


def test_number_of_scrolls(scroll_page):
    scroll_page.actions.goto(Urls.SCROLL)
    max_attempts = 50
    attempts = 0
    while True:
        items = scroll_page.number_of_scrolls()
        if len(items) >= 10:
            break
        if attempts >= max_attempts:
            raise Exception("Too many attempts")
        scroll_page.actions.scroll_into_view(items[-1])
        attempts += 1