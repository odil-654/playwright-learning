from asyncio import wait_for

from pyexpat.errors import messages
import logging


logger = logging.getLogger(__name__)

class PageActions:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        logger.info("Navigate to URL: %s", url)
        self.page.goto(url)

    def reload(self):
        logger.info("Reload current page")
        self.page.reload()

    def bring_to_front(self):
        logger.info("Bring page to front")
        self.page.bring_to_front()

    def close_page(self):
        logger.info("Close current page")
        self.page.close()

    def run_and_accept_alert(self, action):
        logger.info("Run action and accept alert")
        messages = []
        def handle(dialog):
            logger.info("Alert appeared with message: %s", dialog.message)
            messages.append(dialog.message)
            dialog.accept()

        self.page.on("dialog", handle)
        action()
        return messages[0]

    def run_and_dismiss_alert(self, action):
        logger.info("Run action and dismiss alert")
        def handle(dialog):
            logger.info("Dismiss alert with message: %s", dialog.message)
            dialog.dismiss()

        self.page.on("dialog", handle)
        action()

    def run_and_accept_alert_prompt(self, action, text):
        logger.info("Run action and accept prompt with text: %s", text)
        def handle(dialog):
            logger.info("Prompt appeared with message: %s", dialog.message)
            dialog.accept(text)

        self.page.on("dialog", handle)
        action()

    def scroll_into_view(self, element):
        logger.info("Scrolling element into view")
        element.scroll_into_view_if_needed()