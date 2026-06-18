class WebElement():
    def __init__(self, locator, description):
        self.locator = locator
        self.description = description

    def click(self):
        self.locator.click()

    def right_click(self):
        self.locator.right_click()

    def fill(self, text):
        self.locator.fill(text)
