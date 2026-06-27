from asyncio import wait_for


class PageActions:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def reload(self):
        self.page.reload()

    def bring_to_front(self):
        self.page.bring_to_front()

    def close_page(self):
        self.page.close()

    def run_and_accept_alert(self, action):
        def handle(dialog):
            dialog.accept()

        self.page.on("dialog", handle)
        action()

    def run_and_dismiss_alert(self, action):
        def handle(dialog):
            dialog.dismiss()

        self.page.on("dialog", handle)
        action()

    def run_and_accept_alert_prompt(self, action, text):
        def handle(dialog):
            dialog.accept(text)

        self.page.on("dialog", handle)
        action()
