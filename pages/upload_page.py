from core.page_actions import PageActions
from core.web_element import WebElement


class UploadPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.choose_file_button = WebElement(
            self.page.locator("#file-upload"),
            "Upload page -> file choosing button",
        )
        self.success_text = WebElement(
            self.page.locator("h3"),
            "Upload page -> success text"
        )

    def upload_file(self, path):
        return self.choose_file_button.set_input_files(path)
