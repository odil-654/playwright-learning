from core.page_actions import PageActions
from core.web_element import WebElement


class SliderPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.slider = WebElement(
            self.page.locator("input[type='range']"),
            "Slider -> slider locator",
        )

    def click_to_slider(self):
        return self.slider.click()

    def press_slider_to_right(self):
        return self.slider.press_right()

    def press_slider_to_left(self):
        return self.slider.press_left()