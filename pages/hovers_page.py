from core.page_actions import PageActions
from core.web_element import WebElement
from core.multi_web_element import MultiWebElement

class HoversPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.multi_item = MultiWebElement(
            self.page.locator("img[alt='User Avatar']"),
            "Hovers -> Multi item",
        )
        self.hover_text = WebElement(
            self.page.locator("h5:visible"),
            "Hovers -> text after hover",
        )

    def get_all_items(self):
        return self.multi_item.all()

    def hover_and_get_text(self):
        texts = []
        for item in self.multi_item:
            item.hover()
            text = self.hover_text.get_inner_text()
            texts.append(text)
        return texts



