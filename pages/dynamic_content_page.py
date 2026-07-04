from core.page_actions import PageActions
from core.multi_web_element import MultiWebElement


class DynamicContentPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.data_for_src = MultiWebElement(
            self.page.locator("div.large-2 img"),
            "Dynamic content -> Icon"
        )

    def get_all_src(self):
        list_1 = self.data_for_src.all()
        list_2 = []
        for x in list_1:
            list_2.append(x.get_attribute("src"))
        return list_2
