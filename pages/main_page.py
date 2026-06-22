from core.web_element import WebElement

class MainPage:
    def __init__(self, page):
        self.page = page
        self.username_input = WebElement(
            self.page.locator("#username"),
            "Main page -> Username input",
            )
        self.email_input = WebElement(
            self.page.locator("#email"),
            "Main page -> Email input",
        )
        self.password_input = WebElement(
            self.page.locator("#password"),
            "Main page -> Password input",
        )
        self.register_button = WebElement(
            self.page.locator("#register"),
            "Main page -> Register button",
        )

    def fill_form(self, username, email, password):
        self.username_input.fill(username)
        self.email_input.fill(email)
        self.password_input.fill(password)

    def register(self, username, email, password):
        self.fill_form(username, email,password)
        self.register_button.click()

    def transfer_money(self):
        pass

