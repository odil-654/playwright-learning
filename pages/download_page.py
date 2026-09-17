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

    def get_file_name(self, index):
        return self.item_identity.nth(index).get_inner_text()

    def download_file(self, index):
        with self.page.expect_download() as download_info:
            self.item_identity.nth(index).click()

        return download_info.value