class WebElement():
    def __init__(self, locator, description):
        self.locator = locator
        self.description = description

    def click(self):
        self.locator.click()

    def right_click(self):
        self.locator.click(button="right")

    def fill(self, text):
        self.locator.fill(text)

    def get_inner_text(self):
        return self.locator.inner_text()

    def get_text_content(self):
        return self.locator.text_content()

    def press_right(self):
        return self.locator.press("ArrowRight")

    def press_left(self):
        return self.locator.press("ArrowLeft")