from pages.search_result_page import SearchResultsPage


class MainPage:
    def __init__(self, page):
        self.page = page
        self.search_input = page.get_by_test_id("search-input")

    def search_article(self, name):
        self.search_input.fill(name)
        self.search_input.press("Enter")

        return SearchResultsPage(self.page)