def test_slider_with_key(slider_page):
    slider_page.goto("https://the-internet.herokuapp.com/horizontal_slider")
    slider_page.click_to_slider()
    slider_page.press_slider_to_left()
    slider_page.press_slider_to_right()
    slider_page.press_slider_to_right()