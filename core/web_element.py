import logging

logger = logging.getLogger(__name__)


class WebElement:
    def __init__(self, locator, description):
        self.locator = locator
        self.description = description

    def click(self):
        logger.info("Click on element: %s", self.description)
        self.locator.click()

    def right_click(self):
        logger.info("Right click on element: %s", self.description)
        self.locator.click(button="right")

    def fill(self, text):
        logger.info(
            "Fill element: %s with text: %s",
            self.description,
            text,
        )
        self.locator.fill(text)

    def get_inner_text(self):
        logger.info("Get inner text from element: %s", self.description)
        return self.locator.inner_text()

    def get_text_content(self):
        logger.info("Get text content from element: %s", self.description)
        return self.locator.text_content()

    def hover(self):
        logger.info("Hover over element: %s", self.description)
        self.locator.hover()

    def get_attribute(self, name):
        logger.info(
            "Get attribute '%s' from element: %s",
            name,
            self.description,
        )
        return self.locator.get_attribute(name)

    def set_input_files(self, path):
        logger.info(
            "Upload file '%s' to element: %s",
            path,
            self.description,
        )
        self.locator.set_input_files(path)

    def scroll_into_view_if_needed(self):
        logger.info("Scroll to element: %s", self.description)
        self.locator.scroll_into_view_if_needed()

    def press(self, key):
        logger.info(
            "Press '%s' on element: %s",
            key,
            self.description
        )
        self.locator.press(key)
