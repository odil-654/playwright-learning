from core.page_actions import PageActions
from core.web_element import WebElement


class SliderPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.slider = WebElement(
            self.page.locator("input[type='range']"),
            "Slider -> slider locator",
        )
        self.slider_value = WebElement(
            self.page.locator("#range"),
            "Slider -> value display"
        )

    def click_to_slider(self):
        return self.slider.click()

    def press_slider_to_right(self):
        return self.slider.press_right()

    def press_slider_to_left(self):
        return self.slider.press_left()

    def get_slider_value(self):
        return self.slider_value.get_inner_text()

    def get_min(self):
        return  float(self.slider.get_attribute("min"))

    def get_max(self):
        return float(self.slider.get_attribute("max"))

    def get_step(self):
        return float(self.slider.get_attribute("step"))

    def press_slider_to_home(self):
        return self.slider.press_home()