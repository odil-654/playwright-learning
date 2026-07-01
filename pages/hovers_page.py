from core.page_actions import PageActions
from core.web_element import WebElement
from core.multi_web_element import MultiWebElement

class HoversPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.multi_item = MultiWebElement(
            self.page.locator("img[alt='User Avatar']"),
            "Hovers -> Multi item",
        )

    def get_all_items(self):
        return self.multi_item.all()

    def check_all_items(self):
        list_1 = self.get_all_items()
        list_2 = ("name: user", x)
        for x in range(0, len(list_1)):
            assert list_1 == list_2


