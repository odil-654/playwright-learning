from core.page_actions import PageActions
from core.web_element import WebElement


class UploadPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.choose_file_button = WebElement(
            self.page.locator("#file-upload"),
            "Upload page -> file choosing button",
        )
        self.success_text = WebElement(
            self.page.locator("h3"),
            "Upload page -> success text"
        )

    def upload_file(self, path):
        self.choose_file_button.set_input_files(path)

    def get_success_text(self):
        return self.success_text.get_text_content()