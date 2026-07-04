from core.page_actions import PageActions


class FramesPage(PageActions):
    def __init__(self, page):
        super().__init__(page)
        self.upper_left_text = page.frame_locator("[name='frame-top']").frame_locator("[name='frame-left']").locator("body")
        self.upper_middle_text = page.frame_locator("[name='frame-top']").frame_locator("[name='frame-middle']").locator(
            "body")
        self.upper_right_text = page.frame_locator("[name='frame-top']").frame_locator("[name='frame-right']").locator(
            "body")
        self.bottom_text = page.frame_locator("[name='frame-bottom']").locator("body")