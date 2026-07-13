from core.base_url import Urls


def test_check_all_hovers(hovers_page):
    hovers_page.actions.goto(Urls.HOVERS)
    texts = hovers_page.hover_and_get_text()
    for i, text in enumerate(texts):
        assert f"name: user{i+1}" in text

