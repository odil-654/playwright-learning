from core.page_actions import PageActions
from core.web_element import WebElement


class BasicAuthPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.success_message = WebElement(
        self.page.locator("div.example p"),
        "Basic Auth -> Success message",
        )

    def get_success_message(self):
        return self.success_message.get_inner_text()
