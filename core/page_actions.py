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