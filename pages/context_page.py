from core.page_actions import PageActions
from core.web_element import WebElement


class ContextPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.button_context_menu = WebElement(
            self.page.locator("#hot-spot"),
            "Context -> Menu"
        )

    def right_click_context_menu(self):
        return self.run_and_accept_alert(self.button_context_menu.right_click)
