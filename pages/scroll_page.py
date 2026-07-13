from core.page_actions import PageActions
from core.multi_web_element import MultiWebElement

class ScrollPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.scroll_numer_check = MultiWebElement(
            self.page.locator("div.jscroll-added"),
            "Scroll Page -> scroll locator",
        )

    def number_of_scrolls(self):
        list_1 = self.scroll_numer_check.all()
        return list_1
