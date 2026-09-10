from core.page_actions import PageActions
from core.web_element import WebElement


class JavascriptAlertsPage:
    def __init__(self, page):
        self.actions = PageActions(page)
        self.page = page
        self.button_js_alert = WebElement(
            self.page.locator("button[onclick='jsAlert()']"),
            "Alerts -> Click for JS Alert",
        )
        self.button_js_confirm = WebElement(
            self.page.locator("button[onclick='jsConfirm()']"),
            "Alerts -> Click for JS Confirm",
        )
        self.button_js_prompt = WebElement(
            self.page.locator("button[onclick='jsPrompt()']"),
            "Alerts -> Click for JS Prompt"
        )
        self.result = WebElement(
            self.page.locator("#result"),
            "Alerts -> Result Text",
        )

    def get_result_text(self):
        return self.result.get_text_content()

    def click_js_alert(self):
        return self.actions.run_and_accept_alert(self.button_js_alert.click)

    def click_js_confirm(self):
        return self.actions.run_and_accept_alert(self.button_js_confirm.click)

    def click_js_prompt(self, text):
        return self.actions.run_and_accept_alert_prompt(self.button_js_prompt.click, text)

    def click_js_cancel(self):
        return self.actions.run_and_dismiss_alert(self.button_js_confirm.click)
