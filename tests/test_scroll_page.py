def test_number_of_scrolls(scroll_page):
    scroll_page.goto("https://the-internet.herokuapp.com/infinite_scroll")
    text_1 = len(scroll_page.number_of_scrolls())
    while True:
        if text_1 >= 10:
            break
        else:
            scroll_page.scroll_down()
            text_1 = len(scroll_page.number_of_scrolls())

    assert text_1 >= 10