from core.page_actions import PageActions
from core.web_element import WebElement


class NewWindowPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.text_for_reading = WebElement(
            self.page.locator("h3"),
            "Windows page -> New window -> Text",
        )

    def get_text_in_page(self):
        return self.text_for_reading.get_inner_text()