def test_number_of_scrolls(scroll_page):
    scroll_page.goto("https://the-internet.herokuapp.com/infinite_scroll")
    while True:
        items = scroll_page.number_of_scrolls()
        if len(items) >= 10:
            break
        scroll_page.scroll_into_view(items[-1])
    assert len(items) >= 10