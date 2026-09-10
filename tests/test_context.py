from core.base_url import Urls


def test_right_click_for_context_menu(context_page):
    context_page.actions.goto(Urls.CONTEXT_CLICK)
    context_page.right_click_context_menu()
    text_1 = context_page.right_click_context_menu()
    assert text_1 == "You selected a context menu", (
        f"Expected: 'You selected a context menu', "
        f"Actual: '{text_1}'"
    )