from core.page_actions import PageActions
from core.web_element import WebElement


class ContextPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.button_context_menu = WebElement(
            self.page.locator("#hot-spot"),
            "Context -> Menu"
        )

    def right_click_context_menu(self):
        return self.actions.run_and_accept_alert(self.button_context_menu.right_click)
