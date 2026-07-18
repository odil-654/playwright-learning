from core.page_actions import PageActions
from core.web_element import WebElement


class FramesPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.upper_left_text = WebElement(
            page.frame_locator("[name='frame-top']")
            .frame_locator("[name='frame-left']")
            .locator("*"),
            "Frames -> Upper left text",
        )
        self.upper_middle_text = WebElement(
            page.frame_locator("[name='frame-top']")
            .frame_locator("[name='frame-middle']")
            .locator("*"),
            "Frames -> Upper middle text"
        )
        self.upper_right_text = WebElement(
            page.frame_locator("[name='frame-top']")
            .frame_locator("[name='frame-right']")
            .locator("*"),
            "Frames -> Upper right text"
        )
        self.bottom_text = WebElement(
            page.frame_locator("[name='frame-bottom']")
            .locator("*"),
            "Frames -> Bottom text"
        )

    def get_left_frame_text(self):
        return self.upper_left_text.get_text_content()

    def get_right_frame_text(self):
        return self.upper_right_text.get_text_content()

    def get_middle_frame_text(self):
        return self.upper_middle_text.get_text_content()

    def get_bottom_text(self):
        return self.bottom_text.get_text_content()
