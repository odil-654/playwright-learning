from core.multi_web_element import MultiWebElement
from core.page_actions import PageActions


class DownloadPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.item_identity = MultiWebElement(
            self.page.locator("div.example a"),
            "Upload page -> universal file locator",
        )

    def get_all_id(self):
        list_1 = self.item_identity.all()
        return list_1