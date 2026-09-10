from core.base_url import Urls


def test_number_of_scrolls(scroll_page):
    scroll_page.actions.goto(Urls.SCROLL)
    max_attempts = 50
    attempts = 0
    while True:
        items = scroll_page.get_number_of_scrolls()
        if len(items) >= 10:
            break
        if attempts >= max_attempts:
            raise TimeoutError("Too many attempts")
        prev_count = len(items)
        scroll_page.page.click("body")
        scroll_page.actions.scroll_down()
        scroll_page.wait_for_more_paragraphs(prev_count)
        attempts += 1