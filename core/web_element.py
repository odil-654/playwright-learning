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

    def hover(self):
        return self.locator.hover()

    def get_attribute(self, name):
        return self.locator.get_attribute(name)

    def set_input_files(self, path):
        return self.locator.set_input_files(path)