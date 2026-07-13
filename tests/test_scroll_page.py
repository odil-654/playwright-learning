from core.base_url import Urls


def test_number_of_scrolls(scroll_page):
    scroll_page.actions.goto(Urls.SCROLL)
    while True:
        items = scroll_page.number_of_scrolls()
        if len(items) >= 10:
            break
        scroll_page.actions.scroll_into_view(items[-1])
    assert len(items) >= 10