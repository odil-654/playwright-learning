from core.page_actions import PageActions
from core.multi_web_element import MultiWebElement


class ScrollPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.paragraphs = MultiWebElement(
            self.page.locator("div.jscroll-added"),
            "Scroll Page -> scroll locator",
        )

    def get_number_of_scrolls(self):
        list_1 = self.paragraphs.all()
        return list_1

    def wait_for_more_paragraphs(self, prev_count):
        for _ in range(10):
            self.page.wait_for_timeout(1000)
            if len(self.paragraphs.all()) > prev_count:
                return
        raise TimeoutError("Paragraphs did not load")
