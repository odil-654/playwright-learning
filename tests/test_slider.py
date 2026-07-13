from core.base_url import Urls


def test_slider_with_key(slider_page):
    slider_page.actions.goto(Urls.SLIDER)
    slider_page.click_to_slider()
    slider_page.press_slider_to_left()
    slider_page.press_slider_to_right()
    slider_page.press_slider_to_right()
    assert slider_page.get_slider_value() == "3"
