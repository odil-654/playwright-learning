from core.page_actions import PageActions
from core.web_element import WebElement


class WindowsPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.button_for_click = WebElement(
            self.page.locator("a[href='/windows/new']"),
            "Windows page -> Click button"
        )

    def click_and_get_new_page(self):
        with context.expect_page() as page_info:
            page.click("text=Открыть в новой вкладке")