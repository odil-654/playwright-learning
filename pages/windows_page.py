from core.page_actions import PageActions
from core.web_element import WebElement


class WindowsPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.button_for_click = WebElement(
            self.page.locator("a[href='/windows/new']"),
            "Windows page -> Click button"
        )
        self.new_text = WebElement(
            self.page.locator("h3"),
            "Windows page -> New page -> text",
        )

    def click_and_get_new_page(self):
        with self.page.context.expect_page() as page_info:
            self.button_for_click.click()
        new_page = page_info.value
        return new_page