def test_right_click_for_context_menu(context_page):
    context_page.goto("https://the-internet.herokuapp.com/context_menu")
    context_page.right_click_context_menu()
    text_1 = context_page.right_click_context_menu()
    assert text_1 == "You selected a context menu"