from core.page_actions import PageActions
from core.web_element import WebElement


class BasicAuthPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.success_message = WebElement(
        self.page.locator("div.example p"),
        "Basic Auth -> Success message",
        )

    def get_success_message(self):
        return self.success_message.get_inner_text()
