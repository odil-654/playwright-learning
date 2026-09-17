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
            "Slider -> value display",
        )

    def click_to_slider(self):
        self.slider.click()

    def get_slider_value(self):
        return float(self.slider_value.get_inner_text())

    def get_min(self):
        return float(self.slider.get_attribute("min"))

    def get_max(self):
        return float(self.slider.get_attribute("max"))

    def get_step(self):
        return float(self.slider.get_attribute("step"))

    def move_slider_to(self, target_value):
        current_value = self.get_slider_value()
        step = self.get_step()

        steps_count = round(
            abs(target_value - current_value) / step
        )

        if target_value > current_value:
            key = "ArrowRight"
        elif target_value < current_value:
            key = "ArrowLeft"
        else:
            return

        for _ in range(steps_count):
            self.slider.press(key)